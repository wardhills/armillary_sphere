import numpy as np
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy.coordinates import EarthLocation, AltAz, SkyCoord
import astropy.units as u

# Define the 10 brightest stars in the northern hemisphere
brightest_stars = [
    {'name': 'Sirius', 'ra': '06h45m08.9s', 'dec': '-16d42m58s', 'mag': -1.46},
    {'name': 'Vega', 'ra': '18h36m56.3s', 'dec': '+38d47m01s', 'mag': 0.03},
    {'name': 'Arcturus', 'ra': '14h15m39.7s', 'dec': '+19d10m56s', 'mag': -0.05},
    {'name': 'Capella', 'ra': '05h16m41.4s', 'dec': '+45d59m52s', 'mag': 0.08},
    {'name': 'Rigel', 'ra': '05h14m32.3s', 'dec': '-08d12m06s', 'mag': 0.12},
    # {'name': 'Procyon', 'ra': '07h39m18.1s', 'dec': '+05d13m30s', 'mag': 0.34},
    # {'name': 'Betelgeuse', 'ra': '05h55m10.3s', 'dec': '+07d24m25s', 'mag': 0.50},
    # {'name': 'Altair', 'ra': '19h50m47.0s', 'dec': '+08d52m06s', 'mag': 0.76},
    # {'name': 'Aldebaran', 'ra': '04h35m55.2s', 'dec': '+16d30m33s', 'mag': 0.85},
    # {'name': 'Pollux', 'ra': '07h45m19.4s', 'dec': '+28d01m34s', 'mag': 1.14},
]

# Define the dates for the 15th of each month in 2024
dates = [f'2024-{month:02d}-15 00:00:00' for month in range(1, 13)]
times = Time(dates)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Define the observer's location (let's assume Greenwich, UK)
location = EarthLocation(lat=51.4769*u.deg, lon=0.0005*u.deg, height=0*u.m)

# AltAz frame for the observer's location at midnight on each date
altaz_frame = AltAz(obstime=times, location=location)

# Plot setup
plt.figure(figsize=(20, 20))
ax = plt.subplot(111, polar=True)
ax.set_theta_zero_location('N')  # 0 degrees (North) at the top
ax.set_theta_direction(-1)  # Azimuth increases clockwise

# Iterate through each star and calculate their positions
for star in brightest_stars:
    star_coord = SkyCoord(star['ra'], star['dec'], frame='icrs')
    star_altaz = star_coord.transform_to(altaz_frame)
    altitudes = star_altaz.alt.deg
    azimuths = star_altaz.az.deg
    azimuths_rad = np.deg2rad(azimuths)

    # Plot each point with a size proportional to the brightness (inverse of magnitude)
    size = 300 / (star['mag'] + 2)  # Example size scaling, adjust as needed
    ax.scatter(azimuths_rad, altitudes, s=size, label=star['name'])

    # Annotate each point with the corresponding month and altitude (first labeling approach)
    # for i, month in enumerate(months):
    #     label = f'{month} ({altitudes[i]:.1f}°)'
    #     ax.annotate(label, (azimuths_rad[i], altitudes[i]), textcoords="offset points", xytext=(5,5), ha='center')

    # Find the highest altitude and its index
    max_alt_index = np.argmax(altitudes)
    max_altitude = altitudes[max_alt_index]

    # Annotate the highest altitude point with the star name and month
    ax.annotate(f'{star["name"]} ({months[max_alt_index]})',
                (azimuths_rad[max_alt_index], max_altitude),
                textcoords="offset points", xytext=(0,10), ha='center')

    # Draw lines connecting all the points for this star
    ax.plot(azimuths_rad, altitudes, linestyle='-', linewidth=0.5)

# Add legend and title
ax.set_title('Altitude and Azimuth of the Brightest Stars in the Northern Hemisphere at Midnight on the 15th of Each Month in 2024', pad=20)
#plt.legend(loc='upper left', bbox_to_anchor=(1.1, 1.1))
plt.show()
