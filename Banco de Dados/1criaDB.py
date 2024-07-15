# Programa em Python para criar um banco de dados no MYSQL
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha", #definir uma senha para o banco de dados
  auth_plugin='mysql_native_password'
) 

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE nome") #definir um nome para o banco de dados
