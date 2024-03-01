import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)
cursor = conexion.cursor()

def insertarCliente(nombre,email,telefono):
    print("Voy a insertar un cliente")
    print("el nombre es:",nombre.get())
    print("el email es:",email.get())
    print("el telefono es:",telefono.get())
    cursor.execute(f"INSERT INTO clientes VALUES (NULL,'{nombre.get()}','{email.get()}','{telefono.get()}')")
    conexion.commit()
