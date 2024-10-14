import random
import numpy as np


# 1. Funció per crear una matriu de 3x4 de números aleatoris entre 0 i 80
def crear_matriu_aleatoria():
    matriu = np.random.randint(0, 81, size=(3, 4))  # Genera nombres entre 0 i 80 en una matriu de 3x4
    print("Matriu de 3x4 amb números aleatoris de 0 a 80:")
    print(matriu)
    return matriu


# 2. Funció per modificar la matriu: convertir-la a 4x3 i fer que l'última fila passi a ser la última columna
def modificar_matriu(matriu):
    # Convertim la matriu de 3x4 a 4x3
    matriu_modificada = np.zeros((4, 3), dtype=int)  # Matriu buida de 4x3

    # Assignem les primeres 2 columnes directament de les primeres 2 files de la matriu original
    matriu_modificada[:3, :3] = matriu[:, :3]

    # L'última fila de la matriu original passa a ser l'última columna
    matriu_modificada[:, 2] = matriu[2, :]

    print("\nMatriu modificada a 4x3 amb l'última fila convertida a l'última columna:")
    print(matriu_modificada)
    return matriu_modificada


# 3. Funció per fer que tots els valors de la última columna siguin iguals al primer element d'aquesta columna
def modificar_ultima_columna(matriu):
    # Fem que tots els elements de l'última columna siguin iguals al primer element de l'última columna
    primer_element = matriu[0, -1]
    matriu[:, -1] = primer_element

    print("\nMatriu amb l'última columna modificada (tots els valors iguals al primer de la última columna):")
    print(matriu)
    return matriu


# Funció principal per cridar totes les funcions anteriors
def main():
    # Crear matriu de 3x4
    matriu_aleatoria = crear_matriu_aleatoria()

    # Modificar la matriu a 4x3
    matriu_modificada = modificar_matriu(matriu_aleatoria)

    # Modificar la última columna de la nova matriu
    matriu_final = modificar_ultima_columna(matriu_modificada)


