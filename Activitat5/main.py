import matplotlib.pyplot as plt
import pandas as pd

from funcio1_arman import funcio1
from funcio2_arman import funcio2
from funcio3_arman import funcio3
from exerciciB import mainB

def main():
    casos = funcio1()
    morts = funcio2()
    taxa = funcio3()

    paises1 = []

    for index in range(len(casos)):
        pais = casos.loc[index, 'location']
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

    for index in range(len(morts)):
        pais = morts.loc[index, 'location']
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

    for index in range(len(taxa)):
        pais = taxa.loc[index, 'location']
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


main()
mainB()
