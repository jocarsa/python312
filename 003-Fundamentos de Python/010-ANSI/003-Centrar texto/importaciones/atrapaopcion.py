def atrapaOpcion():
    opcion = input("Escoge una opcion: ")
    print(f"La opción escogida es: {opcion}")
    print("\033c")
    if opcion == "1":
        print("Listado de registros")
    elif opcion == "2":
        print("Búsqueda de registros")
    elif opcion == "3":
        print("Inserción de registros")
        nombre = input("Introduce el nombre: ")
        email = input("Introduce el email: ")
        telefono = input("Introduce el telefono: ")
        nuevo_registro = {"nombre":nombre,"email":email,"telefono":telefono}
        print(nuevo_registro)
    elif opcion == "4":
        print("Actualización de registros")
    elif opcion == "5":
        print("Eliminación de registros")
