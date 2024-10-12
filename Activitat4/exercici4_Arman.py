import numpy as np

def matriuRandom():
    matriu = np.random.randint(0, 80, size=(3, 4))  
    return matriu

matriu = matriuRandom()

print(f"Matriu 1: \n", matriu, "\n")

primerNumero = matriu[0, -1]  
segonNumero = matriu[1, -1]   
tercerNumero = matriu[2, -1]  

# axis=1 = columnas, axis=0 = filas
borarColumna = np.delete(matriu, -1, axis=1)

matriuFinal = np.array([
    [borarColumna[0, 0], borarColumna[0, 1] , borarColumna[0, 2]],
    [borarColumna[1, 0] , borarColumna[1, 1], borarColumna[1, 2]],
    [borarColumna[2, 0], borarColumna[2, 1], borarColumna[2, 2]],
    [primerNumero, segonNumero, tercerNumero]
])

print(f"Matriu 2: \n", matriuFinal, "\n")

numero = matriuFinal[3, 0]  

borrarColumna2 = np.delete(matriu, -1, axis=1)

matriuFinal2 = np.array([
    [borrarColumna2[0, 0], borrarColumna2[0, 1], borrarColumna2[0, 2], numero],
    [borrarColumna2[1, 0], borrarColumna2[1, 1], borrarColumna2[1, 2], numero],
    [borrarColumna2[2, 0], borrarColumna2[2, 1], borrarColumna2[2, 2], numero]
])

print(f"Matriu 3: \n", matriuFinal2, "\n")