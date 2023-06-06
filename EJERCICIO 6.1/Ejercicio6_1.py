print("\nCAPITULO 6, EJERCICIO N 1 , CLASES Y OBJETOS\n")

class Vehiculo:
    Color="Rojo"
    Ruedas=4
    Puertas=5
    
class Coche (Vehiculo):
    Velocidad = 60
    Cilindraje= 2000


C=Coche
print("La informacion del Vehiculo es la siguiente")
print("El color del carro es:", C.Color, "\nLa cantidad de Ruedas es:", C.Ruedas, "\nLa cantidad de puertas es:", C.Puertas, "\nLa velocidad es de:", C.Velocidad, "Km/hr", "\nEl cilindraje es:", C.Cilindraje, "Cm3")