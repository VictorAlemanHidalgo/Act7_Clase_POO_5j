print("Programacion POO")
# Definicion de clases
class Perro:
    # Funciones dentro de la clase
    def morder(self):
        print("El perro me mordio")
    
    def DatosPerro(self, nombre, edad):
        print(f"Nombre: {nombre}. Edad: {edad}")


# Zona de creacion de objetos
pitbull = Perro()

# Zona de uso de objetos

pitbull.DatosPerro("Boby", 4)
pitbull.morder()