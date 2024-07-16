#Programa Principal em Python
from flask import Flask, render_template, redirect, request, session, send_file
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session
from flask import render_template
from flask import Flask
from flask import request

from datetime import date, datetime, timedelta
from datetime import time
from dateutil.relativedelta import relativedelta
import mysql.connector
import xlsxwriter

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senha",
  auth_plugin='mysql_native_password',
  database="nome"
)

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route("/", methods=['GET'])
def principal():
    return redirect('index.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():
    nomeNovo = request.form.get('nome', default = '*', type = str)
    mycursor = mydb.cursor()
    sql = "INSERT INTO funcionario (nome) VALUES ('"+nomeNovo+"')"
    mycursor.execute(sql)
    mydb.commit()
    return redirect('index.html')
    

@app.route('/inserirDados', methods=['POST'])
def inserirDados():
    nome = request.form.get('nome',  default = '*', type = str)
    data = request.form.get('dataHoraExtra',  default = '*', type = str)
    hi = request.form.get('horaInicial',  default = '*', type = str)
    hf = request.form.get('horaFinal',  default = '*', type = str)
    diferenca = horaExtra(hi, hf)
    mycursor = mydb.cursor()
    sql2 = "SELECT id_funcionario FROM funcionario WHERE nome = '"+nome+"' LIMIT 1"
    mycursor.execute(sql2)
    myresult = mycursor.fetchone()
    sql = "INSERT INTO horaextra (nome, codigo, dataHoraExtra, horaInicial, horaFinal, diferenca) VALUES ('"+nome+"','"+str(myresult[0])+"','"+data+"', '"+hi+"', '"+hf+"', '"+diferenca+"')" # type: ignore
    mycursor.execute(sql)
    mydb.commit()

    return redirect('index.html')

def converteM(lista):#transforma uma lista[hora, minuto] em minutos
    minutos = lista[0]*60 + lista[1]
    return minutos

def converteH(numero): #transforma minutos em uma lista[Hora, minuto]
    hora = int(numero/60)
    minuto = numero%60
    vetor = str(hora) + ":" + str(minuto)
    return vetor

def stringInt(texto): #transforma um texto em uma lista de numeros
    a = texto.split(':')
    listaInteiro = []
    for i in a:
        listaInteiro.append(int(i))
    return listaInteiro

def horaExtra(hora1, hora2): #Faz a diferença de dois horarios
    soma = 0   
    t1 = converteM(stringInt(hora1))
    t2 = converteM(stringInt(hora2))
    extra = t2 - t1
    soma += extra   
    somaHE = converteH(soma)
    return somaHE

@app.route('/botao', methods=['GET']) # type: ignore
def pega():
    
    mycursor = mydb.cursor()
    sql = "SELECT * FROM horaextra"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    workbook = xlsxwriter.Workbook('Horas Extras.xlsx')
    worksheet = workbook.add_worksheet("My sheet")
    
    worksheet.write('A1', 'Item')
    worksheet.write('B1', 'Nome')
    worksheet.write('C1', 'Código')
    worksheet.write('D1', 'Dia e Hora do Cadastro')
    worksheet.write('E1', 'Data da Hora Extra')
    worksheet.write('F1', 'Hora Inicial')
    worksheet.write('G1', 'Hora Final')
    worksheet.write('H1', 'Diferença') 
    
    row = 1
    col = 0
    for i in range(len(myresult)): # type: ignore
        for y in range(len(myresult[i])):# type: ignore
            worksheet.write(row, col, str(myresult[i][y]))  # type: ignore
            col +=1
        row +=1
        col = 0
        

    workbook.close()
    return 'Sucesso'

@app.route('/pegaNome', methods=['GET'])  # type: ignore
def pegaNome():
    mycursor = mydb.cursor()
    sql = "SELECT nome FROM funcionario"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    return myresult

if __name__ == "__main__": 
    app.run(port=4000)
    