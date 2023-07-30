#Calcular el máximo de números positivos introducidos por teclado, sabiendo que metemos números hasta que introduzcamos uno negativo. El negativo no cuenta.
nm = 0
numero = int(input("Ingrese un numero positivo: "))

while numero >= 0:
    if numero > nm:
        nm = numero

    numero = int(input("Ingrese un numero positivo: "))

print("Los numeros positivos son:", nm)