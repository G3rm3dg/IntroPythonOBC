class Alumno:
    nombre= None
    Calificacion1= None
    Calificacion2= None

    def __init__(self):
        self.nombre = input(("A continuacion digite el Nombre del Alumno: "))
        self.Calificacion1= int(input("La PRIMERA Calificacion del alumno es: "))
        self.Calificacion2= int(input("La SEGUNDA Calificacion del alumno es: "))
        

Al=Alumno()
Pr=(Al.Calificacion1 + Al.Calificacion2)/2
print("\nDE ACUERDO A LOS DATOS SUMISTRADOS, SE ESTABLECE QUE:\n")
print("La Calificacion promedio del Alumno", Al.nombre, "es de: ", Pr)

if Pr>= 6:
    print("\nEl Alumno aprobo la materia")
else:
    print("\nEl Alumno NO aprobo la meteria")

print("\nFIN DEL PROGRAMA")