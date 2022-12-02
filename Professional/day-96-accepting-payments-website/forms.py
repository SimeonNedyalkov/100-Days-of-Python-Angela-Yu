from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user

class RegisterForm(FlaskForm):
    email = StringField('email:')
    password = PasswordField('password:')
    submit = SubmitField('submit')

class LoginForm(FlaskForm):
    email = StringField('email:')
    password = PasswordField('password:')
    submit = SubmitField('submit')