numero = int(input("Introdueix un numero"))

suma = 0;

for i in range(numero+1):
    print(f"{suma} + {i} = {suma+i}")
    suma+=i