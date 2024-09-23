entrada = input("Introdueix entre 1 i 3 paraules separades per espais: ")

paraules = entrada.split()

if len(paraules) < 1 or len(paraules) > 3:
    print("Error: Has de posar entre 1 i 3 paraules.")
else:
    for paraula in paraules:
        caracters = len(paraula)
        primerCaracter = paraula[0]
        ultimCaracter = paraula[-1]
        print(f"La paraula '{paraula}' té {caracters} caràcters, el seu primer caràcter és '{primerCaracter}' i l'últim caràcter és '{ultimCaracter}'")
