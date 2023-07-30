#Determinar cuales son los multiplos de 5 comprendidos entre 1 y N.
N = int(input("Ingrese un numero: "))
na = 1
contador = 0

print("Multiplos de 5 entre 1 y", N, ":")
while na <= N:
    if na % 5 == 0:
        print(na)
        contador += 1
    na += 1
print("Cantidad de multiplos de 5 entre 1 y", N, ":", contador)