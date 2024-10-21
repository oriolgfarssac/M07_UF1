import pandas as pd

# Llista d'IDs seleccionats
selected_ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]

# Carreguem el dataset de mòbils
df = pd.read_csv('mobiles.csv', usecols=['id', 'battery_power', 'fc'])

def show_mega_pixels(ids):
    mega_pixels = df[df['id'].isin(ids)][['id', 'fc']]
    print("Megapixels dels mòbils seleccionats:")
    print(mega_pixels.to_string(index=False))
    return mega_pixels

show_mega_pixels(selected_ids)
