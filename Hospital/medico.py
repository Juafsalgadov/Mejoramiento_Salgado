class Medico:
    def __init__(self, nombre, especialidad, horario, consultorio):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario = horario
        self.consultorio = consultorio

    def mostrarmedico(self):
        print("Médico:", self.nombre)
        self.especialidad.informacionespecialidad()
        self.horario.mostrarhorario()
        self.consultorio.informacionconsultorio()