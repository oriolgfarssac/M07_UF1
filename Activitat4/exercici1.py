import numpy as np

def exercici1():
    matriuCeros = np.arange(50)

    matriu = np.diag(matriuCeros)

    np.save('exercici1.npy',matriu)

    matriu2 = np.load('exercici1.npy')

    return matriu2