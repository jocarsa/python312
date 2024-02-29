import mysql.connector

def insertaRegistro():
    print("Inserción de registros")
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el telefono: ")
    cursor.execute(f"INSERT INTO CLIENTES VALUES (NULL,'{nombre}','{email}','{telefono}')")
    conexion.commit()

def listadoRegistros():
    cursor.execute("SELECT * FROM clientes")
    registros = cursor.fetchall()
    for tupla in registros:
        print("+ ",end='')
        for campo in tupla:
            print(f" - {campo} ",end='')
        print("")
    input("Pulsa una tecla para continuar...")

def eliminaRegistro():
    listadoRegistros()
    id = input("Introduce el id del registro que deseas eliminar: ")
    cursor.execute(f"DELETE FROM clientes WHERE Identificador = {id}")
    conexion.commit()
    input("Eliminación realizada, pulsa una tecla para continuar...")

def actualizaRegistro():
    listadoRegistros()
    id = input("Introduce el id del registro que deseas actualizar: ")
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el telefono: ")
    cursor.execute(f"UPDATE clientes SET nombre='{nombre}',email='{email}',telefono='{telefono}' WHERE Identificador = {id}")
    conexion.commit()

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()

def atrapaOpcion():
    opcion = input("Escoge una opcion: ")
    print(f"La opción escogida es: {opcion}")
    print("\033c")
    if opcion == "1":
        print("Listado de registros")
        listadoRegistros()
    elif opcion == "2":
        print("Búsqueda de registros")
    elif opcion == "3":
        insertaRegistro()
    elif opcion == "4":
        print("Actualización de registros")
        actualizaRegistro()
    elif opcion == "5":
        print("Eliminación de registros")
        eliminaRegistro()
