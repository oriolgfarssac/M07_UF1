import random
import numpy as np


def matriuRandom ():
    dimensio = input("Quina dimensio vols que tingui la matriu? Introdueix els dos nombres junts 12 o 46...")
    files = int(dimensio[0])
    columnes = int(dimensio[1])
    a = np.random.randint(0, 100, size=(files, columnes))
    return a

a = matriuRandom();
print(f"Matriu Original: \n", a, "\n")

def redimensionarMatriu(matriu, files, columnes):
    b = np.resize(matriu, (files, columnes))
    return b

b = redimensionarMatriu(a, 5, 6)
print(f"Matriu Redimensionada: \n", b, "\n")

def valorMaxim(matriu):
    maxim = np.max(matriu)
    return maxim

maxim = valorMaxim(b)
print("Valor Maxim: \n", maxim, "\n")

def valorMinim(matriu):
    minim = np.min(matriu)
    return minim

minim = valorMinim(b)
print("Valor Maxim: \n", minim)