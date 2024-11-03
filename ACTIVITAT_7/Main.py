from connection import getConnection
from create_table import crearTaula
from create import afegirATaula
from read import llegirRegistres
from update import actualitzarRegistre
from delete import eliminarRegistre

print("Menú de Gestió de Registres")
print("1. Crear una taula")
print("2. Crear un nou registre")
print("3. Llegir tots els registres")
print("4. Actualitzar un registre existent")
print("5. Eliminar un registre")
print("6. Sortir")
print()

while True:
    conn = getConnection()
    opcio = input("Selecciona una opció (1-5): ")

    if opcio == '1':
        crearTaula(conn)
    elif opcio == '2':
        afegirATaula(conn)
    elif opcio == '3':
        llegirRegistres(conn)
    elif opcio == '4':
        actualitzarRegistre(conn)
    elif opcio == '5':
        eliminarRegistre(conn)
    else:
        break

