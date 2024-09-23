import random

print("Endevina el nombre entre 1-100")

randomNum = int(random.randint(1, 100))

numero = 0

intents = 1

while numero != randomNum:
        numero = int(input("Prova d'endivinar el numero!"))
        if numero < randomNum:
            print(f"Has fallat el numero es més gran! I portes {intents} intents")
            intents+=1
        if numero > randomNum:
            print(f"Has fallat el numero es més petit! I portes {intents} intents")
            intents+=1
        else:
            print(f"Moltbe el numero era {randomNum}! I l'has endevinat a la {intents}")


