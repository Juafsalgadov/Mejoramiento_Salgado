class Cita:
    def __init__(self, dia, hora, fecha, motivo):
        self.dia = dia
        self.hora = hora
        self.fecha = fecha
        self.motivo = motivo

    def mostrarcita(self):
        print("Cita:")
        print("Dia:", self.dia)
        print("Hora:", self.hora)
        print("Fecha:", self.fecha)
        print("Motivo:", self.motivo)
        