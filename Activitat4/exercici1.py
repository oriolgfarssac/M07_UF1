import numpy as np

matriuCeros = np.arange(50)

matriu = np.diag(matriuCeros)

np.save('exercici1.npy',matriu)

matriu2 = np.load('exercici1.npy')

print("La matriu")
print(matriu2)

dimensioMatriu = matriu.ndim
print(f"La dimensió de la matriu: {dimensioMatriu}")

tamanyMatriu = matriu.shape
print(f"El tamany de la matriu: {tamanyMatriu}")

totalElements = matriu.size
print(f"Número total d’elements: {totalElements}")

tipusElements = matriu.dtype
print(f"Tipus d’elements interns: {tipusElements}")