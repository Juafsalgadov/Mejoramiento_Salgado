#Determinar si un numero es o no es perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio numero es igual a este
numero = int(input("Ingrese un numero para saber si es perfecto: "))
sd = 0
for i in range(1, numero):
    if numero % i == 0:
        sd += i
if sd == numero:
    print(f"{numero} es un numero perfecto.")
else:
    print(f"{numero} no es un numero perfecto.")