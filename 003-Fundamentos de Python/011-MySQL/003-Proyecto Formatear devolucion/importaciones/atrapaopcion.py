import mysql.connector

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
        cursor.execute("SELECT * FROM clientes")
        registros = cursor.fetchall()
        for tupla in registros:
            print("+ ",end='')
            for campo in tupla:
                print(f" - {campo} ",end='')
            print("")
        input("Pulsa una tecla para continuar...")
    elif opcion == "2":
        print("Búsqueda de registros")
    elif opcion == "3":
        print("Inserción de registros")
        nombre = input("Introduce el nombre: ")
        email = input("Introduce el email: ")
        telefono = input("Introduce el telefono: ")
        cursor.execute(f"INSERT INTO CLIENTES VALUES (NULL,'{nombre}','{email}','{telefono}')")
        conexion.commit()
    elif opcion == "4":
        print("Actualización de registros")
    elif opcion == "5":
        print("Eliminación de registros")
