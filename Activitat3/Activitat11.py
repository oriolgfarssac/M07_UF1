divises = {
    "Euro": "€",
    "Dòlar": "$",
    "Lliura": "£",
    "Ien": "¥",
    "Franc Suís": "CHF",
    "Yuan": "¥",
    "Rublo": "₽",
    "Rupia": "₹",
    "Peso": "$",
    "Real": "R$"
}

divisa = input("Introdueix una divisa: ")

if divisa in divises:
    print(f"El símbol de la divisa {divisa} és {divises[divisa]}")
else:
    print(f"La divisa {divisa} no es troba al diccionari.")
