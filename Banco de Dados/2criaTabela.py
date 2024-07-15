

#Comando na linguagem Python para a criação de tabelas no SQL

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  auth_plugin='mysql_native_password',
  database="nome"
)


mycursor = mydb.cursor()
#definição dos tipos de dados, quantidade de colunas e nome das colunas que a tabela terá.

mycursor.execute("CREATE TABLE horaextra (id_horaextra INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255),codigo INT, horaCadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP, dataHoraExtra DATE, horaInicial TIME, horaFinal TIME, diferenca TIME)")
mycursor.execute("CREATE TABLE funcionario (id_funcionario INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255))")