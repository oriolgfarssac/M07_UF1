contactes = {"Oriol": 19, "Dani": 21}

afegirContacte = True;

while afegirContacte:
    nom = str(input("Introdueix el nom del contacte: "))
    edat = int(input("Introdueix l'edat del contacte: "))

    if contactes.get(nom):
        print("Aquest nom ja és a contactes, introdueix un altre nom.")
    else:
        contactes[nom] = edat

    afegirContacte = input("Vols afegir més contactes? (True | False)")
    mostrarContactes = input("Vols mostrar els contactes? (Si | No)")

    if mostrarContactes == "Si":
        print(contactes)
