from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError
import sqlite3 as sql


class LoginForm(FlaskForm):
 email = StringField('Email',validators=[DataRequired(),Email()])
 password = PasswordField('password',validators=[DataRequired()])
 remember = BooleanField('remember Me')
 submit = SubmitField('index')


 def validate_email(self, email):
    con = sql.connect('/database.db')
    conex = con.cursor()
    conex.execute("SELECT email FROM dados_usuario where email = %s",[email.data])
    valemail = conex.fetchone()
    if valemail is None:
      raise ValidationError('Este e-mail não está cadastrado. Cadastre-o antes de fazer login')