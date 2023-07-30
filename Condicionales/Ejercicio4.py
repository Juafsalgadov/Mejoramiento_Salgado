#Pida un numero al usuario que representa días del año. Diga a que mes del año corresponde así. Si el número es menor o igual a 31 indica que esta en enero, Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.
Dias = int(input("Ingrese un nUmero que representa dIas del año: "))
if Dias <= 31:
    mes = "enero"
elif Dias <= 59:
    mes = "febrero"
elif Dias <= 90:
    mes = "marzo"
elif Dias <= 120:
    mes = "abril"
elif Dias <= 151:
    mes = "mayo"
elif Dias <= 181:
    mes = "junio"
elif Dias <= 212:
    mes = "julio"
elif Dias <= 243:
    mes = "agosto"
elif Dias <= 273:
    mes = "septiembre"
elif Dias <= 304:
    mes = "octubre"
elif Dias <= 334:
    mes = "noviembre"
else:
    mes = "diciembre"
print(f"El nUmero de días {Dias} corresponde al mes de {mes}.")