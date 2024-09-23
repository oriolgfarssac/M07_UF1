paraules = input("Introdueix dues paraules separades per espais: ")

paraula1, paraula2 = paraules.split()

if len(paraula1) < 2 or len(paraula2) < 2:
    print("Les paraules han de tenir almenys 2 caràcters.")
else:
    nova_paraula1 = paraula2[:2] + paraula1[2:]
    nova_paraula2 = paraula1[:2] + paraula2[2:]
    print(f"Les noves paraules són: {nova_paraula1} {nova_paraula2}")
