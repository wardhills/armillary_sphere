import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.patches import Annulus, Wedge
from matplotlib import rcParams
rcParams['font.family'] = 'DejaVu Sans'
#rcParams['font.family'] = 'monospace'

zodiac_data = {
    'Aries': {'Symbol': '♈', 'ASCII_Code': 9800, 'Start Date': '2024-04-19', 'End Date': '2024-05-13'},
    'Taurus': {'Symbol': '♉', 'ASCII_Code': 9801, 'Start Date': '2024-05-14', 'End Date': '2024-06-19'},
    'Gemini': {'Symbol': '♊', 'ASCII_Code': 9802, 'Start Date': '2024-06-20', 'End Date': '2024-07-20'},
    'Cancer': {'Symbol': '♋', 'ASCII_Code': 9803, 'Start Date': '2024-07-21', 'End Date': '2024-08-9'},
    'Leo': {'Symbol': '♌', 'ASCII_Code': 9804, 'Start Date': '2024-08-10', 'End Date': '2024-09-15'},
    'Virgo': {'Symbol': '♍', 'ASCII_Code': 9805, 'Start Date': '2024-09-16', 'End Date': '2024-10-30'},
    'Libra': {'Symbol': '♎', 'ASCII_Code': 9806, 'Start Date': '2024-10-31', 'End Date': '2024-11-22'},
    'Scorpius': {'Symbol': '♏', 'ASCII_Code': 9807, 'Start Date': '2024-11-23', 'End Date': '2024-11-29'},
    #'Ophiuchus': {'Symbol': '⛎', 'ASCII_Code': 9934, 'Start Date': '2024-11-30', 'End Date': '2024-12-17'},
    #'Ophiuchus': {'Symbol': '\u26CE', 'ASCII_Code': 9934, 'Start Date': '2024-11-30', 'End Date': '2024-12-17'},
    'Ophiuchus': {'Symbol': 'oph', 'ASCII_Code': 9934, 'Start Date': '2024-11-30', 'End Date': '2024-12-17'},
    'Sagittarius': {'Symbol': '♐', 'ASCII_Code': 9808, 'Start Date': '2024-12-18', 'End Date': '2024-01-18'},
    'Capricornus': {'Symbol': '♑', 'ASCII_Code': 9809, 'Start Date': '2024-01-19', 'End Date': '2024-02-15'},
    'Aquarius': {'Symbol': '♒', 'ASCII_Code': 9810, 'Start Date': '2024-02-16', 'End Date': '2024-03-11'},
    'Pisces': {'Symbol': '♓', 'ASCII_Code': 9811, 'Start Date': '2024-03-12', 'End Date': '2024-04-18'}
}

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]


def plot_annulus_with_labels() -> None:
    annulus_width = 10
    r_inner = 275
    r_outer = r_inner + annulus_width
    zodiac_ext_radius = r_outer + annulus_width/2  # Slightly increased radius for zodiac

    fig, ax = plt.subplots(figsize=(20, 20), dpi=300)  # Increased figure size
    cir_1 = Annulus((0, 0), r_inner, r_outer - r_inner, alpha=0.7, color="white")
    ax.add_patch(cir_1)
    ax.set(xlim=(-r_outer - 20, r_outer + 20), ylim=(-r_outer - 20, r_outer + 20))  # Increased limits

    # Plot month divisions and labels
    start_month = 1
    day_numbers = [datetime.date(2024, month, start_month).timetuple().tm_yday for month in range(1, 13)]
    start_month_angles = [(day_number * (360 / 365)) for day_number in day_numbers]

    # Add shaded wedge for each month with alternate coloring
    for i, start_angle in enumerate(start_month_angles):
        end_angle = start_month_angles[i + 1] if i + 1 < len(start_month_angles) else 360
        color = 'lightgray' if i % 2 == 0 else 'darkgray'
        wedge = Wedge((0, 0), r_inner+5, start_angle, end_angle, width=annulus_width, color=color, alpha=1)
        ax.add_patch(wedge)

        # Adding month labels
        mid_angle = (start_angle + end_angle) / 2
        x = (r_inner) * np.cos(np.radians(mid_angle))
        y = (r_inner) * np.sin(np.radians(mid_angle))
        ax.text(x, y, months[i], ha='center', va='center', fontsize=12, rotation=mid_angle-90, color='black', fontweight='bold')

    # Plot zodiac signs
    for i,(sign, data) in enumerate(zodiac_data.items()):
        start_day_number = datetime.datetime.strptime(data['Start Date'], '%Y-%m-%d').timetuple().tm_yday
        end_day_number = datetime.datetime.strptime(data['End Date'], '%Y-%m-%d').timetuple().tm_yday
        if start_day_number > end_day_number:
            end_day_number += 365

        start_angle = (start_day_number * (360 / 365))
        end_angle = (end_day_number * (360 / 365))

        color = 'lightgray' if i % 2 == 0 else 'darkgray'
        wedge = Wedge((0, 0), zodiac_ext_radius, start_angle, end_angle, width=annulus_width, color=color, alpha=1)
        ax.add_patch(wedge)

        avg_angle = (start_angle + end_angle) / 2
        x = (zodiac_ext_radius - annulus_width / 2) * np.cos(np.radians(avg_angle))
        y = (zodiac_ext_radius - annulus_width / 2) * np.sin(np.radians(avg_angle))
        ax.text(x, y, data['Symbol'], ha='center', va='center', fontsize=16, fontweight='bold', rotation=avg_angle-90, font='monospace', color='black')
    #    ax.text(x, y, chr(data['ASCII_Code']), ha='center', va='center', font = 'monospace', fontsize=16, fontweight='bold', rotation=avg_angle - 90, color='black')

    # Add day ticks
    for day in range(1, 366):
        day_angle = (day * (360 / 365))
        x_inner = (r_inner -5) * np.cos(np.radians(day_angle))
        y_inner = (r_inner -5) * np.sin(np.radians(day_angle))
        x_outer = (r_inner ) * np.cos(np.radians(day_angle))
        y_outer = (r_inner ) * np.sin(np.radians(day_angle))

        ax.plot([x_inner, x_outer], [y_inner, y_outer], color='black', linewidth=0.7, zorder=3, alpha=0.5)

    plt.axis('off')
    plt.savefig("Annulus_with_labels_refined_adjusted.png")
    plt.savefig("Annulus_with_labels_refined_adjusted.svg")
    plt.show()

plot_annulus_with_labels()
