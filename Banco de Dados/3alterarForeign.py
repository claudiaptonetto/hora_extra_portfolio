#Comando na linguagem Python para a modificar a chave estrangeira da tabela no SQL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  auth_plugin='mysql_native_password',
  database="nome"
)


mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE horaextra ADD FOREIGN KEY(codigo) REFERENCES funcionario(id_funcionario) ON DELETE SET NULL")
