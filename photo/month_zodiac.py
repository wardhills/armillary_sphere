import datetime

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

def get_day_number(year: int = 2024, day_of_month: int = 1)-> list[float]:

    day_numbers = []

    for month in range(1, 13):
        # Get the first day of the month
        day = datetime.date(year, month, day_of_month)
        # Get the day number in the year (1-365)
        day_number = day.timetuple().tm_yday
        day_numbers.append(day_number)
    return day_numbers


def get_angles(day_numbers: list[float]) -> list[float]:
    return [round((day_number *(360/365)),1) for day_number in day_numbers]

if __name__ == '__main__':

    # day_numbers = get_day_number(year=2024, day_of_month=15)
    #
    # print(get_angles(day_numbers))
    #
    # for constellation, data in zodiac_data.items():
    #     day_number = get_day_number_from_string(data['Date'])
    #     angle = get_angles([day_number])[0]
    #     print(f'{constellation}, {data["Symbol"]}, {data["ASCII_Code"]}, {data["Date"]}, Day Number: {day_number}, Angle: {angle}')

    r_inner = 275
    r_outer = 285

    cir_1 = Annulus((0, 0), 1., 0.05,alpha=.7,fc="grey")        # large circular annulus

    fig, ax = plt.subplots(figsize=(5,5),dpi=100)

    ax.add_patch(cir_1)
    ax.set(xlim=(-1,1),ylim=(-1,1))
   # ax.grid()
    ax.set_title("Ecliptic Ring")
   # ax.set_aspect('equal')
    plt.savefig("Ecliptic Ring.png")

    plt.show()





