
nums = input("Introdueix 10 numeros separats per un espai: ")


numsList = nums.split()

contadorNumeros = len(numsList)


if contadorNumeros < 10:
    print("Has de posar 10 numeros")

else:
    numsTupla = tuple(int(num) for num in numsList)

print(numsTupla)
