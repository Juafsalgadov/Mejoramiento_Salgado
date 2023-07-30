#Solicite la hora en formato horas, minutos y segundos. Imprima en pantalla la hora que será dentro de 1 segundo
horas = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
st = horas * 3600 + minutos * 60 + segundos

st += 1
nh = st // 3600
st %= 3600
nm = st // 60
st %= 60
ns = st
print("La hora dentro de 1 segundo sera:", "{:02d}:{:02d}:{:02d}".format(nh, nm, ns))