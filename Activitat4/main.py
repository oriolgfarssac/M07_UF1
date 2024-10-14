from exercici1 import exercici1
import exercici2
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


# Funció per mostrar la informació de les matrius de l'exercici 2
def info_matriu(matriu, nom_matriu):
    # Mostrar la matriu
    print(f"\nMatriu de l'exercici2   {nom_matriu}:")
    for fila in matriu:
        print(fila)

    # Número total d'elements
    total_elements = sum(len(fila) for fila in matriu) if isinstance(matriu[0], list) else len(matriu)
    print(f"Total d'elements a la matriu {nom_matriu}: {total_elements}")

    # Dimensió de la matriu (files, columnes)
    if isinstance(matriu[0], list):
        dimensions = (len(matriu), len(matriu[0]))
    else:
        dimensions = (1, len(matriu))
    print(f"Dimensió de la matriu {nom_matriu}: {dimensions} (files, columnes)")

    # Tipus d'elements interns
    tipus_element = type(matriu[0][0]) if isinstance(matriu[0], list) else type(matriu[0])
    print(f"Tipus d'elements interns a la matriu {nom_matriu}: {tipus_element}")

    # Tamany de la matriu
    tamany = total_elements
    print(f"Tamany de la matriu {nom_matriu}: {tamany}")



matriu1 = exercici2.creacioarray1()
matriu2 = exercici2.creacioarray2()
matriu3 = exercici2.creacioarray3()


info_matriu(matriu1, "1")
info_matriu(matriu2, "2")
info_matriu(matriu3, "3")


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





