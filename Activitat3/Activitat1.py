
n = int(input("Intodueix un numero entre 10 i 100"))

if 10 <= n <= 100:
    numeros = tuple(range(0, n + 1))
    print(numeros)
else:
    print("El numero introduit no es troba entre 10 i 100")