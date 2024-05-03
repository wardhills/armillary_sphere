import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.ticker import MultipleLocator

def plot_annulus_scales():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Constants
    radius_outer = 1.0
    radius_inner = 0.8
    angle_range = 360

    # Function to draw annulus scales
    def draw_annulus_scale(angle_start, angle_end, radius, scale_count, label, unit_count=1, unit_label=''):
        theta = np.linspace(np.radians(angle_start), np.radians(angle_end), scale_count + 1)
        for i in range(scale_count):
            x = [radius * np.cos(theta[i]), radius * np.cos(theta[i + 1])]
            y = [radius * np.sin(theta[i]), radius * np.sin(theta[i + 1])]
            ax.plot(x, y, color='black')
            if (i % unit_count == 0):
                mid_angle = (theta[i] + theta[i + 1]) / 2
                x_text = (radius + 0.05) * np.cos(mid_angle)
                y_text = (radius + 0.05) * np.sin(mid_angle)
                ax.text(x_text, y_text, f"{i * unit_label}", ha='center', va='center')

    # Plot annulus scales
    draw_annulus_scale(0, angle_range, radius_outer, angle_range, 'Degrees', unit_count=30, unit_label='°')
    draw_annulus_scale(0, angle_range, radius_inner, 24 * 60, 'Time (24-hour format)')
    draw_annulus_scale(0, angle_range, radius_inner - 0.1, 24 * 60, 'Time (decimal hours)', unit_count=60, unit_label='h')

    # Set axis limits
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')

    # Remove axis
    ax.axis('off')

    plt.show()

# Call the function to plot annulus scales
plot_annulus_scales()
