# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)

cursor = conexion.cursor()
cursor.execute("INSERT INTO clientes VALUES (NULL,'Jose Vicente','info@josevicentecarratala.com','620891718')")

conexion.commit()
