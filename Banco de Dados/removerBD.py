
#Comando na linguagem Python para remover o banco de dados.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  auth_plugin='mysql_native_password',  
)



mycursor = mydb.cursor()

sql = "DROP DATABASE nome"

mycursor.execute(sql)
