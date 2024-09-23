euros = int(input("introdueixi un valor en €"))

iva = int(input("Introdueix un IVA (4%, 10% o 21%)"))

while iva != 4 and iva != 10 and iva != 21:
    iva = int(input("Introdueix un IVA dels següents (4%, 10% o 21%)"))

print(f"Has introduit {euros}€, has escollit un IVA del {iva}% i et dona un resultat de {(euros*(iva+100))/100}")