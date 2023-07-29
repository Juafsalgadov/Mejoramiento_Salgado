from consultorio import *
from horario import *
from medico import *
from consulta import *
from paciente import *
from cita import *
from especialidad import *

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

class Consultorio:
    def __init__(self, nombre):
        self.nombre = nombre

    def informacionconsultorio(self):
        print("Consultorio:", self.nombre)
    
class Especialidad:
    def __init__(self, nombre):
        self.nombre = nombre

    def informacionespecialidad(self):
        print("Especialidad:", self.nombre)
    
class Horario:
    def __init__(self, disponibilidad):
        self.disponibilidad = disponibilidad

    def mostrarhorario(self):
        print("Horario:", self.disponibilidad)
    
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
    
class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.citas = []

    def mostrarpaciente(self):
        print("Paciente:", self.nombre)
        print("Citas:")
        for cita in self.citas:
            cita.mostrarcita()
            
consultorio1 = Consultorio("Consultorio A")
horario1 = Horario("Lunes a Viernes, de 9:00 a 17:00")
especialidad1 = Especialidad("Pediatría")
medico1 = Medico("Dr. Garcia", especialidad1, horario1, consultorio1)
paciente1 = Paciente("Ana")
cita1 = Cita("Lunes", "10:00", "2023-07-31", "Control de rutina")

paciente1.citas.append(cita1)
medico1.mostrarmedico()
paciente1.mostrarpaciente()