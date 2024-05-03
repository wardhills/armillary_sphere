import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import get_sun, AltAz, EarthLocation, SkyCoord
from astropy.time import Time
from astropy import units as u

# Define the observer's location (e.g., New York City)
observer_location = EarthLocation(lat=40.7128*u.deg, lon=-74.0060*u.deg, height=0*u.m)

# Create an array of times covering the entire year
times = Time(np.arange('2024-01-01', '2025-01-01', dtype='datetime64[D]'))

# Calculate the sunrise positions for each day
sunrise_positions = get_sun(times).transform_to(AltAz(obstime=times, location=observer_location))

# Convert sunrise positions to ecliptic coordinates
ecliptic_coords = sunrise_positions.transform_to('geocentrictrueecliptic')

# Extract ecliptic longitude
ecliptic_longitude = ecliptic_coords.lon.wrap_at(180 * u.deg).degree

# Plot the positions on the ecliptic
plt.figure(figsize=(10, 5))
plt.plot(ecliptic_longitude, marker='o', linestyle='None')
plt.xlabel('Days since Jan 1, 2024')
plt.ylabel('Ecliptic Longitude (degrees)')
plt.title('Sunrise Positions on the Ecliptic (New York City)')
plt.grid(True)
plt.show()
