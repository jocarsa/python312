# pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="programagestion",
    password="programagestion",
    database="programagestion"
)
