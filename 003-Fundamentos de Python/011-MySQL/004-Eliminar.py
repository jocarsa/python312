# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()
cursor.execute("DELETE FROM clientes WHERE Identificador = 3")

conexion.commit()
