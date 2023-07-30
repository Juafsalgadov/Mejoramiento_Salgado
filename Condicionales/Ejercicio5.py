from datetime import date

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

Hoy = date.today()
fecha = date(año, mes, dia)
diferencia = Hoy - fecha
if diferencia.days < 0:
    print("Faltan", abs(diferencia.days), "días para llegar a la fecha ingresada.")
elif diferencia.days > 0:
    print("Han pasado", diferencia.days, "días desde la fecha ingresada hasta hoy.")
else:
    print("La fecha ingresada es hoy.")