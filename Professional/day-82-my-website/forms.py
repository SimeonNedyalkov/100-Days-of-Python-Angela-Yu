from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    email = StringField('Email: ')
    password = PasswordField("Password: ")
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email= StringField('Email:')
    password= PasswordField('Password:')
    submit = SubmitField('Register')