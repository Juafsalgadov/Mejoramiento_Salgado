#Lista con contador
numeros = [1, 2, 3, 4, 5, 3, 2, 1, 2, 2]
Ncontador = 2
contador = 0
for numero in numeros:
    if numero == Ncontador:
        contador += 1
print("El elemento", Ncontador, "aparece", contador, "veces en la lista.")