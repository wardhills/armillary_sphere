import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Annulus

zodiac_data  = {
    'Aries': {'Symbol': '♈', 'ASCII_Code': 9800, 'Date': '2024-04-19'},
    'Taurus': {'Symbol': '♉', 'ASCII_Code': 9801, 'Date': '2024-05-14'},
    'Gemini': {'Symbol': '♊', 'ASCII_Code': 9802, 'Date': '2024-06-20'},
    'Cancer': {'Symbol': '♋', 'ASCII_Code': 9803, 'Date': '2024-07-21'},
    'Leo': {'Symbol': '♌', 'ASCII_Code': 9804, 'Date': '2024-08-10'},
    'Virgo': {'Symbol': '♍', 'ASCII_Code': 9805, 'Date': '2024-09-16'},
    'Libra': {'Symbol': '♎', 'ASCII_Code': 9806, 'Date': '2024-10-31'},
    'Scorpius': {'Symbol': '♏', 'ASCII_Code': 9807, 'Date': '2024-11-23'},
    'Ophiuchus': {'Symbol': '⛎', 'ASCII_Code': 9934, 'Date': '2024-11-30'},
    'Sagittarius': {'Symbol': '♐', 'ASCII_Code': 9808, 'Date': '2024-12-18'},
    'Capricornus': {'Symbol': '♑', 'ASCII_Code': 9809, 'Date': '2025-01-19'},
    'Aquarius': {'Symbol': '♒', 'ASCII_Code': 9810, 'Date': '2025-02-16'},
    'Pisces': {'Symbol': '♓', 'ASCII_Code': 9811, 'Date': '2025-03-12'}
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def get_day_number_from_string(date: str) -> int:
    year, month, day = map(int, date.split('-'))
    date_obj = datetime.date(year, month, day)
    return date_obj.timetuple().tm_yday

def get_day_number(year: int = 2024, day_of_month: int = 1) -> list[float]:
    day_numbers = []
    for month in range(1, 13):
        # Get the first day of the month
        day = datetime.date(year, month, day_of_month)
        # Get the day number in the year (1-365)
        day_number = day.timetuple().tm_yday
        day_numbers.append(day_number)
    return day_numbers

def get_angles(day_numbers: list[float]) -> list[float]:
    return [round((day_number *(360/365)), 1) for day_number in day_numbers]

def plot_annulus_with_labels():
    r_inner = 275
    r_outer = 285

    cir_1 = Annulus((0, 0), r_inner, r_outer - r_inner, alpha=0.7, color="white")  # large circular annulus

    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)

    ax.add_patch(cir_1)
    ax.set(xlim=(-r_outer, r_outer), ylim=(-r_outer, r_outer))

    # Plot zodiac sign labels
    day_numbers = get_day_number()
    angles = get_angles(day_numbers)
    for i, month in enumerate(months):
        angle = np.radians(angles[i])
        x = (r_outer + 10) * np.cos(angle)
        y = (r_outer + 10) * np.sin(angle)
        ax.text(x, y, month, ha='center', va='center', fontsize=8)

    for sign, data in zodiac_data.items():
        day_number = get_day_number_from_string(data['Date'])
        angle_idx = day_number - 1
        if angle_idx >= len(angles):
            angle_idx = len(angles) - 1
        angle = np.radians(angles[angle_idx])
        x = (r_outer + 20) * np.cos(angle)  # Adjust position for zodiac symbols
        y = (r_outer + 20) * np.sin(angle)  # Adjust position for zodiac symbols
        ax.text(x, y, f"{data['Symbol']} - {day_number}", ha='center', va='center', fontsize=8)

    ax.set_title("Annulus labeled with Month, Zodiac Symbol, and Day of the year")
    plt.axis('off')  # Turn off axis
    plt.savefig("Annulus_with_labels.png")
    plt.show()

plot_annulus_with_labels()
