import mysql.connector
import shutil
AMARILLO = '\033[93m'
RESET = '\033[0m'
def insertaRegistro():
    
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el telefono: ")
    cursor.execute(f"INSERT INTO CLIENTES VALUES (NULL,'{nombre}','{email}','{telefono}')")
    conexion.commit()
    print(f"{AMARILLO}Pulsa una tecla para continuar...{RESET}")
    input()

def listadoRegistros():
    columnas, filas = shutil.get_terminal_size()
    for i in range(0,columnas):
        print("-",end='')
    cursor.execute("SHOW COLUMNS FROM clientes")
    titulos = cursor.fetchall()
    cuentafila = 4
    numerocolumnas = len(titulos)
    cuentacolumna = 0
    for titulo in titulos:
        poscol = round((cuentacolumna/numerocolumnas)*columnas)
        print(f"\033[{cuentafila};{poscol}H|",titulo[0],end='')
        cuentacolumna += 1
    for i in range(0,columnas):
        print("-",end='')
    cuentafila = 6
    cursor.execute("SELECT * FROM clientes")
    registros = cursor.fetchall()
    for tupla in registros:
        cuentacolumna = 0
        numerocolumnas = len(tupla)
        for campo in tupla:
            poscol = round((cuentacolumna/numerocolumnas)*columnas)
            print(f"\033[{cuentafila};{poscol}H|",campo,end='')
            #print(f" - {campo} ",end='')
            cuentacolumna += 1
        print("")
        cuentafila += 1
    print(f"{AMARILLO}Pulsa una tecla para continuar...{RESET}")
    input()

def buscaRegistros():
    buscanombre = input("Introduce el nombre a buscar: ")
    cursor.execute(f"SELECT * FROM clientes WHERE nombre LIKE '%{buscanombre}%'")
    registros = cursor.fetchall()
    for tupla in registros:
        print("+ ",end='')
        for campo in tupla:
            print(f" - {campo} ",end='')
        print("")
    print(f"{AMARILLO}Pulsa una tecla para continuar...{RESET}")
    input()

def eliminaRegistro():
    listadoRegistros()
    id = input("Introduce el id del registro que deseas eliminar: ")
    cursor.execute(f"DELETE FROM clientes WHERE Identificador = {id}")
    conexion.commit()
    input("Eliminación realizada.")
    print(f"{AMARILLO}Pulsa una tecla para continuar...{RESET}")
    input()

def actualizaRegistro():
    listadoRegistros()
    id = input("Introduce el id del registro que deseas actualizar: ")
    nombre = input("Introduce el nombre: ")
    email = input("Introduce el email: ")
    telefono = input("Introduce el telefono: ")
    cursor.execute(f"UPDATE clientes SET nombre='{nombre}',email='{email}',telefono='{telefono}' WHERE Identificador = {id}")
    conexion.commit()
    print(f"{AMARILLO}Pulsa una tecla para continuar...{RESET}")
    input()

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()
