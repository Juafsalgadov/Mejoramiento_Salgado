numeros = []
numerosing = int(input("Ingrese los numeros de ingreso: "))
for j in range(numerosing):
    numero = int(input(f"Ingrese el numero {j + 1}: "))
    numeros.append(numero)
contador = int(input("Ingrese el numeroque desee contar: "))
contado = numeros.count(contador)
print(f"El numero {contador} aparece {contado} veces en la lista.")