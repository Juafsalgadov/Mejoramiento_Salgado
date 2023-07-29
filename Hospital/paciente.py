class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.citas = []

    def mostrarpaciente(self):
        print("Paciente:", self.nombre)
        print("Citas:")
        for cita in self.citas:
            cita.mostrarcita()