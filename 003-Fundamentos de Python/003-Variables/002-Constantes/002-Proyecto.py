'''
Programa de gestión
v0.1 Jose Vicente Carratalá
'''
# Declaraciones
NOMBRE_PROGRAMA = "Programa de gestión"
VERSION_Y_AUTOR = "v0.1 Jose Vicente Carratalá"
# Pantalla de inicio
print(NOMBRE_PROGRAMA)
print(VERSION_Y_AUTOR)
input("Pulsa una tecla para continuar...")
#Menú de navegación
print("1.-Listar registros")
print("2.-Buscar registros")
print("3.-Introducir un registro")
print("4.-Actualizar un registro")
print("5.-Eliminar un registro")
opcion = input("Escoge una opcion: ")
print(f"La opción escogida es: {opcion}")
