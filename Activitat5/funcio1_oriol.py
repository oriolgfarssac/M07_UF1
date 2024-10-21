import pandas as pd

# Llista d'IDs seleccionats
selected_ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

# Carreguem el dataset de mòbils
df = pd.read_csv('mobiles.csv', usecols=['id', 'clock_speed'])

def show_clock_speed(ids):
    clock_speeds = df[df['id'].isin(ids)][['id', 'clock_speed']]
    print("Clock Speed dels mòbils seleccionats:")
    print(clock_speeds.to_string(index=False))
    return clock_speeds

show_clock_speed(selected_ids)
