from flask import Flask
from flask import render_template, url_for, flash, redirect
import sqlite3 as sql 
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user
from forms import LoginForm

app = Flask(__name__)
app.debug=True

login_manager = LoginManager(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id, email, password): 
         self.id = (id)
         self.email = email
         self.password = password
         self.authenticated = False

    def is_active(self):
         return self.is_active()

    def is_anonymous(self):
         return False

    def is_authenticated(self):
         return self.authenticated

    def is_active(self):
         return True

    def get_id(self):
       return self.id

@login_manager.user_loader
def load_user(user_id):
   con = sql.connect('/database.db')
   conex = con.cursor()
   conex.execute("SELECT * from dados_usuario where email = %s",[user_id])
   logus = conex.fetchone()
   if  logus is None:
      return None
   else:
      return User(logus[user_id])

@app.route("/ login", methods=['GET','POST'])
def login():
   if current_user.is_authenticated:
      return redirect (url_for ('home'))
   form = LoginForm()
   if form. validate_on_submit():
      con = sql.connect('/database.db')
      conex = con.cursor()
      conex.execute("SELECT * from dados_usuario where email = %s",[form.email.data])
      user = list(conex.fetchone())
      Us = load_user(user[0])
      if form.email.data == Us.email and form.password.data == Us.password:
         login_user(Us, remember=form.remember.data)
         Umail = list({form.email.data})[0].split('@')[0]
         flash('logado com sucesso' +Umail)
         return redirect(url_for('home'))
      else:
         flash('Login inválido')
   return render_template('index.html', form = form)

