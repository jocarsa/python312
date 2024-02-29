# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

registros = cursor.fetchall()

for tupla in registros:
    print(tupla)

conexion.commit()
