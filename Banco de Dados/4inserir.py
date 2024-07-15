
#Comando na linguagem Python para inserir dados na tabela criada.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  auth_plugin='mysql_native_password',
  database="nome"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO horaextra (nome, codigo ,dataHoraExtra, horaInicial, horaFinal, diferenca) VALUES ('Fulano de Tal', '1' ,'2022-11-30', '05:30:00', '07:30:00', '02:00:00'  )")
#teste para verificar funcionamento do banco de dados.

mydb.commit()

print(mycursor.rowcount, "Registro inserido")
