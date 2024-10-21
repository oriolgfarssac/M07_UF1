import pandas as pd

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



