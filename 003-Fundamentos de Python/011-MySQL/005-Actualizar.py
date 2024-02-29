# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()
cursor.execute("UPDATE clientes SET nombre = 'Jose Vicente Carratalá Sanchis' WHERE nombre = 'Jose Vicente'")

conexion.commit()
