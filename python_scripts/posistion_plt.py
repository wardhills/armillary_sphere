import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
import astropy.units as u

# Define the dates for the 15th of each month in 2024
dates = [f'2024-{month:02d}-15 00:00:00' for month in range(1, 13)]
times = Time(dates)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define the observer's location (let's assume Greenwich, UK)
location = EarthLocation(lat=51.4769*u.deg, lon=0.0005*u.deg, height=0*u.m)

# AltAz frame for the observer's location at midnight on each date
altaz_frame = AltAz(obstime=times, location=location)

# Define the coordinates of the constellation Lyra (approximated by the position of Vega)
# Vega's approximate RA/Dec (J2000) is 18h36m56s +38d47m01s
vega = SkyCoord('18h36m56s +38d47m01s', frame='icrs')

# Convert Vega's position to the AltAz frame
vega_altaz = vega.transform_to(altaz_frame)

# Extract the altitude and azimuth
altitudes = vega_altaz.alt.deg
azimuths = vega_altaz.az.deg

# Convert azimuths to radians for the polar plot
azimuths_rad = np.deg2rad(azimuths)

# Create the polar plot
plt.figure(figsize=(10, 10))
ax = plt.subplot(111, polar=True)

# Plot altitude vs. azimuth
ax.scatter(azimuths_rad, altitudes, label='Vega (Lyra)')

# Annotate each point with the corresponding month
for i, month in enumerate(months):
    ax.annotate(month, (azimuths_rad[i], altitudes[i]), textcoords="offset points", xytext=(5,5), ha='center')

# Customize the plot
ax.set_theta_zero_location('N')  # 0 degrees (North) at the top
ax.set_theta_direction(-1)  # Azimuth increases clockwise

# Add labels and title
ax.set_title('Altitude and Azimuth of Vega (Lyra) at Midnight on the 15th of Each Month in 2024', pad=20)
ax.set_xlabel('Azimuth (degrees)')
ax.set_ylabel('Altitude (degrees)', labelpad=20)

# Add radial ticks
ax.set_rlabel_position(135)  # Position of radial labels

# Show the plot
plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
# from astropy.time import Time
# from astropy.coordinates import EarthLocation, AltAz, get_sun, SkyCoord
# from astropy.coordinates import ICRS, FK5
# import astropy.units as u
#
# # Define the dates for the 15th of each month in 2024
# dates = [f'2024-{month:02d}-15 00:00:00' for month in range(1, 13)]
# times = Time(dates)
#
# # Define the observer's location (let's assume Greenwich, UK)
# location = EarthLocation(lat=51.4769*u.deg, lon=0.0005*u.deg, height=0*u.m)
#
# # AltAz frame for the observer's location at midnight on each date
# altaz_frame = AltAz(obstime=times, location=location)
#
# # Define the coordinates of the constellation Lyra (approximated by the position of Vega)
# # Vega's approximate RA/Dec (J2000) is 18h36m56s +38d47m01s
# vega = SkyCoord('18h36m56s +38d47m01s', frame='icrs')
#
# # Convert Vega's position to the AltAz frame
# vega_altaz = vega.transform_to(altaz_frame)
#
# # Plot the positions
# plt.figure(figsize=(10, 5))
# plt.plot(times.datetime, vega_altaz.alt, 'o-', label='Altitude of Vega')
# plt.xlabel('Date')
# plt.ylabel('Altitude (degrees)')
# plt.title('Altitude of Vega (Lyra) at Midnight on the 15th of Each Month in 2024')
# plt.legend()
# plt.grid()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
