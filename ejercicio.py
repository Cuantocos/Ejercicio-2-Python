class Alumno():
    nombre = None
    nota = None
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrarNombreDeAlumno(self):
        print(self.nombre)

    def mostrarNotaDeAlumno(self):
        print(self.nota)

    def cambiarNombreDeAlumno(self, nuevoNombre):
        self.nombre = nuevoNombre

    def cambiarNotaDeAlumno(self, nuevaNota):
        self.nota = nuevaNota

    def aprobo(self):
        if self.nota < 6:
            print("El alumno desaprobo la materia")
        else:
            print("El alumno aprobo la materia")

alumnoSantiago = Alumno("Santiago", 8)
alumnoSantiago.mostrarNombreDeAlumno()
alumnoSantiago.mostrarNotaDeAlumno()
alumnoSantiago.aprobo()
alumnoSantiago.cambiarNotaDeAlumno(5)
alumnoSantiago.aprobo()
alumnoSantiago.cambiarNombreDeAlumno("Pepe")
alumnoSantiago.mostrarNombreDeAlumno()