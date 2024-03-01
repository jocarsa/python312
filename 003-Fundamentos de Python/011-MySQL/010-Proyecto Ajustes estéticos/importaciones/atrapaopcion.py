from importaciones.operacionesmysql import *

def atrapaOpcion():
    AZUL = '\033[94m'
    RESET = '\033[0m'
    
    opcion = input("Escoge una opcion: ")
    print(f"La opción escogida es: {opcion}")
    print("\033c")
    if opcion == "1":
        print(f"{AZUL}Listado de registros{RESET}")
        listadoRegistros()
    elif opcion == "2":
        print(f"{AZUL}Búsqueda de registros{RESET}")
        buscaRegistros()
    elif opcion == "3":
        print(f"{AZUL}Inserción de registros{RESET}")
        insertaRegistro()
    elif opcion == "4":
        print(f"{AZUL}Actualización de registros{RESET}")
        actualizaRegistro()
    elif opcion == "5":
        print(f"{AZUL}Eliminación de registros{RESET}")
        eliminaRegistro()
