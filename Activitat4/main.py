from exercici1 import exercici1
from exercici4_Arman import matriuRandom
from exercici4_Arman import segonaMatriu
from exercici4_Arman import terceraMatriu
from exercici3 import matriuRandomO
from exercici3 import redimensionarMatriu
from exercici3 import valorMaxim
from exercici3 import valorMinim
from exercici4_Oriol import crear_matriu
from exercici4_Oriol import modificar_matriu
from exercici4_Oriol import modificar_ultima_columna

matriu = exercici1()

print("Exercici 1 del Arman", "\n" )
print("Del exercici 1 la matriu", "\n" , matriu, "\n")

dimensioMatriu = matriu.ndim
print(f"Del exercici 1 la dimensió de la matriu: {dimensioMatriu}", "\n")

tamanyMatriu = matriu.shape
print(f"Del exercici 1 el tamany de la matriu: {tamanyMatriu}", "\n")

totalElements = matriu.size
print(f"Del exercici 1 el Número total d’elements: {totalElements}", "\n")

tipusElements = matriu.dtype
print(f"Del exercici 1 el Tipus d’elements interns: {tipusElements}", "\n")


print("Exercici 4 del Arman", "\n" )
matriuRandom = matriuRandom()
print(f"Exercici 4 Arman Matriu de 3x4 de números aleatoris de 0 a 80: \n", matriuRandom, "\n")


matriu2 = segonaMatriu(matriuRandom)
print(f"Exercici 4 Arman la última columna passa a ser la última fila: \n", matriu2, "\n")


matriu3 = terceraMatriu(matriu2)
print(f"Exercici 4 Arman La nova matriu haurà de tindre els mateixos números en la última columna (han de ser iguals al primer número de la última columna de la matriu anterior): \n", matriu3, "\n")

matriuOriol = matriuRandomO()

print("Exercici 3 de l'Oriol", "\n" )
print("Del exercici 3 la matriu random es ", "\n" , matriuOriol, "\n")
matriuOriol = redimensionarMatriu(matriuOriol, 1, 2)
print("Del exercici 3 la matriu redimensionada es ", "\n" , matriuOriol, "\n")
valorMaximE3 = valorMaxim(matriuOriol)
print("Del exercici 3 el valor maxim es ", "\n" , valorMaximE3, "\n")
valorMinimE3 = valorMinim(matriuOriol)
print("Del exercici 3 el valor minim es ", "\n" , valorMinimE3, "\n")
ex4Oriol = crear_matriu()
print("Del exercici 4 la matriu es", "\n" , ex4Oriol, "\n")
ex4Oriol = modificar_matriu(ex4Oriol)
print("Del exercici 4 la matriu modificada es", "\n" , ex4Oriol, "\n")
ex4Oriol = modificar_ultima_columna(ex4Oriol)
print("Del exercici 4 la matriu amb l'ultima columna modificada es", "\n" , ex4Oriol, "\n")





