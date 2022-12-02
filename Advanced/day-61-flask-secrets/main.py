import flask_wtf
from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,Length
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired(), Length(8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "secret12345"
Bootstrap(app)

@app.route("/")
def home():
    login_form = LoginForm()

    return render_template('index.html', form=login_form)

@app.route('/login', methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email_data = login_form.email.data
        password_data = login_form.password.data
        return render_template('success.html', form=login_form, email_data=email_data,password_data=password_data)
    elif login_form.validate_on_submit() == False:
        email_data = login_form.email.data
        password_data = login_form.password.data
        return render_template('denied.html', form=login_form, email_data=email_data,password_data=password_data)




if __name__ == '__main__':
    app.run(debug=True)
