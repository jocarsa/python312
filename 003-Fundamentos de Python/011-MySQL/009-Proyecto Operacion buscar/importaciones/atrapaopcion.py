from importaciones.operacionesmysql import *

def atrapaOpcion():
    opcion = input("Escoge una opcion: ")
    print(f"La opción escogida es: {opcion}")
    print("\033c")
    if opcion == "1":
        print("Listado de registros")
        listadoRegistros()
    elif opcion == "2":
        print("Búsqueda de registros")
        buscaRegistros()
    elif opcion == "3":
        insertaRegistro()
    elif opcion == "4":
        print("Actualización de registros")
        actualizaRegistro()
    elif opcion == "5":
        print("Eliminación de registros")
        eliminaRegistro()
