import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Llista d'IDs seleccionats
selected_ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

df = pd.read_csv('mobiles.csv', usecols=['id', 'clock_speed', 'fc', 'battery_power'])

def show_clock_speed(ids):
    clock_speeds = df[df['id'].isin(ids)][['id', 'clock_speed']]
    print("Clock Speed dels mòbils seleccionats:")
    print(clock_speeds.to_string(index=False))
    return clock_speeds

def show_mega_pixels(ids):
    mega_pixels = df[df['id'].isin(ids)][['id', 'fc']]
    print("Megapixels dels mòbils seleccionats:")
    print(mega_pixels.to_string(index=False))
    return mega_pixels

def show_battery_power(ids):
    battery_power = df[df['id'].isin(ids)][['id', 'battery_power']]
    print("Clock Speed dels mòbils seleccionats:")
    print(battery_power.to_string(index=False))
    return battery_power


def plot_data(clock_speed, mega_pixels, battery_power):
    ids = clock_speed['id'].values
    clock_speed_values = clock_speed['clock_speed'].values
    mega_pixels_values = mega_pixels['fc'].values
    battery_power_values = battery_power['battery_power'].values

    x = np.arange(len(ids))

    width = 0.15

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width, clock_speed_values, width, label='Clock Speed (GHz)')
    ax.bar(x, mega_pixels_values, width, label='Megapixels (fc)')
    ax.bar(x + width, battery_power_values, width, label='Battery Power (mAh)')

    ax.set_xlabel('Mobile ID')
    ax.set_ylabel('Values')
    ax.set_title('Comparación de características de móviles seleccionados')
    ax.set_xticks(x)
    ax.set_xticklabels(ids)
    ax.legend()
    plt.tight_layout()
    ax.set_yscale('log')  # Cambia a escala logarítmica
    plt.ylim(1, 2000)
    plt.show()


def main():
    clock_speed = show_clock_speed(selected_ids)
    mega_pixels = show_mega_pixels(selected_ids)
    battery_power = show_battery_power(selected_ids)
    plot_data(clock_speed, mega_pixels, battery_power)

main()