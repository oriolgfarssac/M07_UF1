import pandas as pd
import matplotlib.pyplot as plt



# Creem el DataFrame
df = pd.read_csv("List of world cities by population density.csv")


# 1. Funció per mostrar el total de població per ciutat
def mostrar_poblacio(df):



# 2. Funció per calcular la densitat per km² per ciutat
def densitat_per_km2(df):



# 3. Funció per calcular la densitat per m² per ciutat
def densitat_per_m2(df):



# 4. Funció main per mostrar gràfiques circulars
def main():
    # Cridem a les funcions que mostren els resultats
    mostrar_poblacio(df)
    densitat_per_km2(df)
    densitat_per_m2(df)



    # Afegir llegendes
    plt.tight_layout()
    plt.show()






