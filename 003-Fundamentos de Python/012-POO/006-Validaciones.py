class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
    def saluda(self):
        return("Hola que tal")
    def getEdad(self):
        return edad
    def setEdad(self,nuevaedad):
        if nuevaedad == self.edad + 1:
            self.edad = nuevaedad
        else:
            print("operación no permitida")

Persona1 = Persona()
Persona1.nombre = "Jose Vicente"
Persona1.edad = 45


print(f"El nombre de esta persona es: {Persona1.nombre}")
print(f"La edad de esta persona es: {Persona1.edad}")
print(f"{Persona1.nombre} te está saludando y te dice: {Persona1.saluda()}")

Persona1.setEdad(55)

print(f"La edad de esta persona es: {Persona1.edad}")
