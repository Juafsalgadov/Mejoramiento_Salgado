class Consulta:
    def __init__(self, dia, hora, fecha, paciente, medico):
        self.dia = dia
        self.hora = hora
        self.fecha = fecha
        self.paciente = paciente
        self.medico = medico

    def informacionconsulta(self):
        print("Consulta:")
        print("Día:", self.dia)
        print("Hora:", self.hora)
        print("Fecha:", self.fecha)
        print("Paciente:", self.paciente.nombre)
        print("Médico:", self.medico.nombre)