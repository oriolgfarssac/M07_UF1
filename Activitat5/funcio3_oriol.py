import pandas as pd

# Llista d'IDs seleccionats
selected_ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

# Carreguem el dataset de mòbils
df = pd.read_csv('mobiles.csv', usecols=['id', 'battery_power'])

def show_battery_power(ids):
    battery_power = df[df['id'].isin(ids)][['id', 'battery_power']]
    print("Clock Speed dels mòbils seleccionats:")
    print(battery_power.to_string(index=False))
    return battery_power

show_battery_power(selected_ids)
