import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lista de IDs seleccionados
selected_ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]


df = pd.read_csv('mobiles.csv', usecols=['id', 'clock_speed', 'fc', 'battery_power'])

def show_clock_speed(ids):
    clock_speeds = df[df['id'].isin(ids)][['id', 'clock_speed']]
    print("Clock Speed de los móviles seleccionados:")
    print(clock_speeds.to_string(index=False))
    return clock_speeds

def show_mega_pixels(ids):
    mega_pixels = df[df['id'].isin(ids)][['id', 'fc']]
    print("Megapixels de los móviles seleccionados:")
    print(mega_pixels.to_string(index=False))
    return mega_pixels

def show_battery_power(ids):
    battery_power = df[df['id'].isin(ids)][['id', 'battery_power']]
    print("Battery Power de los móviles seleccionados:")
    print(battery_power.to_string(index=False))
    return battery_power

def grafic_clock_speed(clock_speed):
    plt.figure(figsize=(10, 6))
    plt.bar(clock_speed['id'], clock_speed['clock_speed'], color='blue', width=5)
    plt.xlabel('Mobile ID')
    plt.ylabel('Clock Speed (GHz)')
    plt.title('Clock Speed dels móvils sel·lecciónats')
    plt.ylim(0, 5)
    plt.grid()
    plt.show()

def grafic_mega_pixels(mega_pixels):
    plt.figure(figsize=(10, 6))
    plt.bar(mega_pixels['id'], mega_pixels['fc'], color='orange', width=5)
    plt.xlabel('Mobile ID')
    plt.ylabel('Megapixels (fc)')
    plt.title('Megapixels dels móvils sel·lecciónats')
    plt.ylim(0, 20)
    plt.grid()
    plt.show()

def grafic_battery_power(battery_power):
    plt.figure(figsize=(10, 6))
    plt.bar(battery_power['id'], battery_power['battery_power'], color='green', width=5)
    plt.xlabel('Mobile ID')
    plt.ylabel('Battery Power (mAh)')
    plt.title('Battery Power dels móvils sel·lecciónats')
    plt.ylim(0, 2000)
    plt.grid()
    plt.show()

def mainOriol():
    clock_speed = show_clock_speed(selected_ids)
    mega_pixels = show_mega_pixels(selected_ids)
    battery_power = show_battery_power(selected_ids)

    grafic_clock_speed(clock_speed)
    grafic_mega_pixels(mega_pixels)
    grafic_battery_power(battery_power)

