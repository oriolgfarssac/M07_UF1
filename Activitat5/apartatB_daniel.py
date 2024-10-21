import pandas as pd
import matplotlib.pyplot as plt


# Funció per netejar valors que continguin corxets, agafant només el número abans del primer corxet
def netejar_poblacio(val):
    # Separem pel primer corxet
    val_netejat = val.split('[')[0]
    # Eliminar qualsevol coma i convertir a int
    return int(val_netejat.replace(',', ''))


# Carregar el fitxer de dades
def carregar_dades_fitxer(nom_fitxer):
    df = pd.read_csv(nom_fitxer)
    # Aplicar la funció de neteja a la columna de Població
    df['Population'] = df['Population'].apply(netejar_poblacio)
    # Fem servir només les 10 primeres ciutats
    df = df[['City', 'Population', 'Area (km²)', 'Density (/km²)']].head(10)
    return df


# Funció que mostra la població per ciutat
def mostrar_poblacio(df):
    print("Total de població per ciutat:")
    print(df[['City', 'Population']])


# Funció que mostra la densitat per km² per ciutat
def mostrar_densitat_km2(df):
    print("Densitat per KM² per ciutat:")
    print(df[['City', 'Density (/km²)']])


# Funció que mostra la densitat per m² per ciutat (convertim la densitat de km² a m²)
def mostrar_densitat_m2(df):
    df['Density (/m²)'] = df['Density (/km²)'] / 1_000_000
    print("Densitat per M² per ciutat:")
    print(df[['City', 'Density (/m²)']])


# Funció que crea les gràfiques circulars
def crear_grafiques(df):
    # Gràfica per a la població
    plt.figure(figsize=(8, 6), num="Població per ciutat")
    plt.pie(df['Population'], labels=df['City'], autopct='%1.1f%%')
    plt.title("Distribució de la població per ciutat")
    plt.legend(loc='best')
    plt.show()

    # Gràfica per a la densitat per km²
    plt.figure(figsize=(8, 6), num="Densitat per km² per ciutat")
    plt.pie(df['Density (/km²)'], labels=df['City'], autopct='%1.1f%%')
    plt.title("Distribució de la densitat per km² per ciutat")
    plt.legend(loc='best')
    plt.show()

    # Gràfica per a la densitat per m²
    plt.figure(figsize=(8, 6), num="Densitat per m² per ciutat")
    plt.pie(df['Density (/km²)'] / 1_000_000, labels=df['City'], autopct='%1.1f%%')
    plt.title("Distribució de la densitat per m² per ciutat")
    plt.legend(loc='best')
    plt.show()


# Funció principal que crida les altres
def mainDani():
    # Carreguem el fitxer
    df = carregar_dades_fitxer('List of world cities by population density.csv')

    # Mostrem la informació
    mostrar_poblacio(df)
    mostrar_densitat_km2(df)
    mostrar_densitat_m2(df)

    # Creem les gràfiques circulars
    crear_grafiques(df)



