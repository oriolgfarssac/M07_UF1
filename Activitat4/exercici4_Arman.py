import numpy as np

#funcio que crea una matriu amb numeros random de 3x4
def matriuRandom():
    matriu = np.random.randint(0, 80, size=(3, 4))  
    return matriu


matriu = matriuRandom()

#funcio que pasa la ultima columna a fila
def segonaMatriu(matriu):

    primerNumero = matriu[0, -1]  
    segonNumero = matriu[1, -1]   
    tercerNumero = matriu[2, -1]  

    borarColumna = np.delete(matriu, -1, axis=1)

    matriuFinal = np.array([
        [borarColumna[0, 0], borarColumna[0, 1] , borarColumna[0, 2]],
        [borarColumna[1, 0] , borarColumna[1, 1], borarColumna[1, 2]],
        [borarColumna[2, 0], borarColumna[2, 1], borarColumna[2, 2]],
        [primerNumero, segonNumero, tercerNumero]
    ])

    return matriuFinal

#funcio que agafa el primer numero de la tercera columna, i afageix una nova columna amb el numero pillat 
def terceraMatriu(matriu):
    
    matriuFinal2 = np.array([
        [matriu[0, 0], matriu[0, 1], matriu[0, 2], matriu[0, 2]],
        [matriu[1, 0], matriu[1, 1], matriu[1, 2], matriu[0, 2]],  
        [matriu[2, 0], matriu[2, 1], matriu[2, 2], matriu[0, 2]]   
    ])
    return matriuFinal2