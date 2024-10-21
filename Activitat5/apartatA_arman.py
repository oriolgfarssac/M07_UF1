import pandas as pd
from matplotlib import pyplot as plt


def funcio1():

    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'total_cases'])

    paisos = ['Afghanistan', 'Armenia', 'China', 'Georgia', 'Liberia', 'Guatemala', 'Tanzania', 'Turkmenistan', 'Uruguay', 'Zimbabwe']

    filaPais = []

    for i in range(len(df)):
        if df.loc[i, 'location'] in paisos:
            filaPais.append(df.loc[i])

    # DataFrame on es guarda nomes les files del paisos seleccionats
    dfPaisos = pd.DataFrame(filaPais)

    meses = ['2021-01', '2021-02', '2021-03', '2021-04']

    filas = []

    for i in range(len(dfPaisos)):
        mes_actual = dfPaisos.iloc[i]['date'][:7]
        if mes_actual in meses:
            filas.append(dfPaisos.iloc[i])

    # DataFrame on es guarda nomes les files amb els paisos i els mesos seleccionats
    dfPaisosMesos = pd.DataFrame(filas)

    resultats = []

    for i in range(len(paisos)):
        for mes in meses:

            filtrePais = dfPaisosMesos['location'] == paisos[i]

            filtreMes = dfPaisosMesos['date'].str[:7] == mes

            casos = dfPaisosMesos[filtrePais & filtreMes]['total_cases']

            suma = casos.sum()

            resultats.append({'location': paisos[i], 'month': mes, 'total_cases': suma})

    # Dataframe on es guarda el resultat
    resultats_df = pd.DataFrame(resultats)
    return resultats_df




def funcio2():

    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'total_deaths'])

    paisos = ['Afghanistan', 'Armenia', 'China', 'Georgia', 'Liberia', 'Guatemala', 'Tanzania', 'Turkmenistan', 'Uruguay', 'Zimbabwe']

    filaPais = []

    for i in range(len(df)):
        if df.loc[i, 'location'] in paisos:
            filaPais.append(df.loc[i])

    # DataFrame on es guarda nomes les files del paisos seleccionats
    dfPaisos = pd.DataFrame(filaPais)

    meses = ['2021-01', '2021-02', '2021-03', '2021-04']

    filas = []

    for i in range(len(dfPaisos)):
        mes_actual = dfPaisos.iloc[i]['date'][:7]
        if mes_actual in meses:
            filas.append(dfPaisos.iloc[i])

    # DataFrame on es guarda nomes les files amb els paisos i els mesos seleccionats
    dfPaisosMesos = pd.DataFrame(filas)

    resultats = []

    for i in range(len(paisos)):
        for mes in meses:

            filtrePais = dfPaisosMesos['location'] == paisos[i]

            filtreMes = dfPaisosMesos['date'].str[:7] == mes

            morts = dfPaisosMesos[filtrePais & filtreMes]['total_deaths']

            suma = morts.sum()

            resultats.append({'location': paisos[i], 'month': mes, 'total_deaths': suma})

    # Dataframe on es guarda el resultat
    resultats_df = pd.DataFrame(resultats)
    return resultats_df



def funcio3():

    df = pd.read_csv('df_covid19_countries.csv', usecols=['location', 'date', 'reproduction_rate'])

    paisos = ['Afghanistan', 'Armenia', 'China', 'Georgia', 'Liberia', 'Guatemala', 'Tanzania', 'Turkmenistan', 'Uruguay', 'Zimbabwe']

    filaPais = []

    for i in range(len(df)):
        if df.loc[i, 'location'] in paisos:
            filaPais.append(df.loc[i])

    # DataFrame on es guarda nomes les files del paisos seleccionats
    dfPaisos = pd.DataFrame(filaPais)

    meses = ['2021-01', '2021-02', '2021-03', '2021-04']

    filas = []

    for i in range(len(dfPaisos)):
        mes_actual = dfPaisos.iloc[i]['date'][:7]
        if mes_actual in meses:
            filas.append(dfPaisos.iloc[i])

    # DataFrame on es guarda nomes les files amb els paisos i els mesos seleccionats
    dfPaisosMesos = pd.DataFrame(filas)

    resultats = []

    for i in range(len(paisos)):
        for mes in meses:

            filtrePais = dfPaisosMesos['location'] == paisos[i]

            filtreMes = dfPaisosMesos['date'].str[:7] == mes

            taxa = dfPaisosMesos[filtrePais & filtreMes]['reproduction_rate']

            suma = 0

            for valor in taxa:
                suma = suma + valor

            resultats.append({'location': paisos[i], 'month': mes, 'reproduction_rate': suma})

    # Dataframe on es guarda el resultat
    resultats_df = pd.DataFrame(resultats)
    return resultats_df





def mainArman():
    casos = funcio1()
    morts = funcio2()
    taxa = funcio3()

    paises1 = []

    for i in range(len(casos)):
        pais = casos.loc[i, 'location']
        if pais not in paises1:
            paises1.append(pais)


    for pais in paises1:
        datos = casos[casos['location'] == pais]
        plt.plot(datos['month'], datos['total_cases'], label=pais)


    plt.title('Total de casos por mes y pais')
    plt.xlabel('Mes')
    plt.ylabel('Total de casos')
    plt.legend()
    plt.show()


    paises2 = []

    for i in range(len(morts)):
        pais = morts.loc[i, 'location']
        if pais not in paises2:
            paises2.append(pais)

    for pais in paises2:
        datos = morts[morts['location'] == pais]
        plt.plot(datos['month'], datos['total_deaths'], label=pais)

    plt.title('Total de morts per mes y pais')
    plt.xlabel('Mes')
    plt.ylabel('Total de morts')
    plt.legend()
    plt.show()




    paises3 = []

    for i in range(len(taxa)):
        pais = taxa.loc[i, 'location']
        if pais not in paises3:
            paises3.append(pais)

    for pais in paises3:
        datos = taxa[taxa['location'] == pais]
        plt.plot(datos['month'], datos['reproduction_rate'])

    plt.title('Tasa de reproduccio per mes per pais')
    plt.xlabel('Mes')
    plt.ylabel('Tasa de reproduccio')
    plt.legend()
    plt.show()
