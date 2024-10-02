areas_pis = {
    "Menjador": 10.15,
    "Rebedor": 9.56,
    "Habitació1": 12.34,
    "Terrassa": 15.55,
    "Lavabo": 7.98,
    "Cuina": 12.00, 
    "Habitació2": 12.23
}

print("Segon element:", list(areas_pis.keys())[1])

print("Últim element:", list(areas_pis.keys())[-1])

print("Àrea de la terrassa:", areas_pis["Terrassa"])

print("Del primer element al tercer element:", list(areas_pis.keys())[:3])

print("Del tercer element a l'últim:", list(areas_pis.keys())[2:])

total_area_habitacions = areas_pis["Habitació1"] + areas_pis["Habitació2"]
print("Total de l'àrea de les dues habitacions:", total_area_habitacions)

areas_pis["Lavabo"] = 8.50
print("Nova llista d'àrees:", areas_pis)

