import numpy as np
import random


# Crear una matriu de 3x4 amb números aleatoris de 0 a 80
def crear_matriu():
    matriu = np.random.randint(0, 81, size=(3, 4))
    print("Matriu original:")
    print(matriu)
    return matriu


# Modificar la matriu a 4x3 i la última fila passa a ser la última columna
def modificar_matriu(matriu):
    matriu_modificada = np.transpose(matriu)
    print("\nMatriu modificada 4x3 (última fila convertida en última columna):")
    print(matriu_modificada)
    return matriu_modificada


# Modificar la matriu perque la última columna ha de tenir els mateixos números
def modificar_ultima_columna(matriu_modificada):
    primer_valor_ultima_columna = matriu_modificada[0, -1]
    matriu_modificada[:, -1] = primer_valor_ultima_columna
    print(f"\nMatriu modificada amb última columna igual a {primer_valor_ultima_columna}:")
    print(matriu_modificada)
    return matriu_modificada


# Funció principal que crida les altres funcions
def main():

    matriu = crear_matriu()
    primer_valor_ultima_columna = matriu[0, -1]
    matriu_modificada = modificar_matriu(matriu)
    matriu_final = modificar_ultima_columna(matriu_modificada)

main()
