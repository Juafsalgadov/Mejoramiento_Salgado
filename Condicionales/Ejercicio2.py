#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa
numero = int(input("Ingrese un numero entre 0 y 9999: "))
if numero < 0 or numero > 9999:
    print("El numero ingresado excede los limites.")
else:
    if numero < 10:
        print("El numero tiene 1 cifra.")
    elif numero < 100:
        print("El numero tiene 2 cifras.")
    elif numero < 1000:
        print("El numero tiene 3 cifras.")
    elif numero < 10000:
        print("El numero tiene 4 cifras.")