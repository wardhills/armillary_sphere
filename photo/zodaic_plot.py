import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import MonthLocator, DateFormatter

# Function to calculate the zodiac sign
def zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

# Get current date
now = datetime.now()

# Number of days in each month
days_in_month = [31, 28 if now.year % 4 != 0 or (now.year % 100 == 0 and now.year % 400 != 0) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Calculate cumulative days
cumulative_days = np.cumsum(days_in_month)

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Plot 360-degree marks
ax.plot(np.linspace(0, 2*np.pi, 360), np.ones(360), color='black', alpha=0.2)

# Plot day of the month
day_of_month = (now.day - 1 + now.hour / 24 + now.minute / (24 * 60)) / days_in_month[now.month - 1]
ax.plot(day_of_month * 2 * np.pi, 1, marker='o', color='blue')

# Plot month
ax.plot((cumulative_days[now.month - 1] - 1 + now.hour / 24 + now.minute / (24 * 60)) * 2 * np.pi / 365, 1.05, marker='o', color='red')

# Plot zodiac
zodiac = zodiac_sign(now.month, now.day)
zodiac_angles = {
    "Aries": 0,
    "Taurus": 30,
    "Gemini": 60,
    "Cancer": 90,
    "Leo": 120,
    "Virgo": 150,
    "Libra": 180,
    "Scorpio": 210,
    "Sagittarius": 240,
    "Capricorn": 270,
    "Aquarius": 300,
    "Pisces": 330
}
ax.plot(zodiac_angles[zodiac] * np.pi / 180, 1.1, marker='o', color='green')

# Set the title
ax.set_title(f"Today: {now.strftime('%B')} {now.day}, Zodiac: {zodiac}", va='bottom')

# Set the y-axis limits
ax.set_ylim(0, 1.2)

# Remove the y-axis labels
ax.set_yticklabels([])

# Show the plot
plt.show()
