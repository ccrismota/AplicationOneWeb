from flask import Flask, render_template, request
import sqlite3 as sql
import os

currentdirectory = os.path.dirname(os.path.abspath(__file__)) 

app = Flask(__name__)
app.config['SECRET_KEY']='aplicationOne'


@app.route('/')
def index():
  nome_usuario = "visitante"
  return render_template('index.html', nome_usuario = nome_usuario)

@app.route('/cadastro')
def cadastro():
  return render_template('usuario.html')


@app.route('/home')
#@login_required
def home():
  return render_template('home.html')

@app.route('/registro',methods = ['POST', 'GET'])
def registro():
  mensagem = 'mensagem'
  if request.method == 'POST':
    try:
        nome_completo = request.form['nome_completo']
        email = request.form['email']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        cep = request.form['cep']
        rua = request.form['rua']
        numero = request.form['numero']
        complemento = request.form['complemento']
        cpf = request.form['cpf']
        pis = request.form['pis']
        senha = request.form['senha']

        with sql.connect("database.db") as con:
          conex = con.cursor()
          query1 = "INSERT INTO dados_usuario  VALUES ('{nm}', '{em}', '{pa}', '{es}', '{mu}', '{ce}','{ru}', '{nu}', '{co}', '{cp}', '{pi}', '{se}')".format(nm=nome_completo, em=email, pa=pais, es=estado, mu=municipio, ce=cep, ru=rua, nu=numero, co=complemento, cp=cpf, pi=pis, se=senha)
          conex.execute(query1)
          con.commit()
          mensagem = "Dados adicionados com sucesso"
    except:   
        sql.connect("database.db").rollback()
        mensagem = "erro na operação!!!"  
    finally:   
        return render_template("result.html", mensagem = mensagem) 
      
        
sql.connect("database.db").close()

@app.route('/listdb')
def listar():
  conn = sql.connect("database.db")
  conn.row_factory = sql.Row

  conex = conn.cursor()
  conex.execute("SELECT * FROM dados_usuario")

  dados_usuario = conex.fetchall();
  return render_template('listdb.html',dados_usuario = dados_usuario)

if __name__ == '__main__':
    app.run(debug=True)  
""" if __name__ == "__main__":
 app.run(host='0.0.0.0',port=8080,threaded=True) """
 
 
