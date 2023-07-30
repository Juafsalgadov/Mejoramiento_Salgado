#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?
np = 0
pa = 1
while pa <= 1000:
    sd = 0
    for i in range(1, pa):
        if pa % i == 0:
            sd += i

    if sd == pa:
        np += 1
        print("Numero perfecto:", pa)

    pa += 1

print("Cantidad de numeros perfectos de 1 a 1000:", np)