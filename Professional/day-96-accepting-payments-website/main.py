from flask import Flask,request,url_for,render_template,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from flask_login import LoginManager,UserMixin,login_user,logout_user,current_user
from forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash
import stripe
import json


app = Flask(__name__)
# SQLalchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret123key@'

YOUR_DOMAIN = 'http://localhost:4242'

# Stripe config
app.config['STRIPE_PUBLIC_KEY']= 'pk_test_51M7eJaCjDgYExzfYmmPj7oeIMnmjiAreIGquCURHcCyrPOTI9GS6Hg8FKPDp3bRm4yo5pvf5mZPkUfiLWndNPrwP00MQloBXoH'
app.config['STRIPE_SECRET_KEY']= 'sk_test_51M7eJaCjDgYExzfYPoO0j4pLsbWV7JVoUiGBtDBMI8OpqPEomiAxjIbVC5YyrT63Ma4IYtOFGPkDSly5lNsiI4dz00nyPkkbKZ'
stripe.api_key = 'sk_test_51M7eJaCjDgYExzfYPoO0j4pLsbWV7JVoUiGBtDBMI8OpqPEomiAxjIbVC5YyrT63Ma4IYtOFGPkDSly5lNsiI4dz00nyPkkbKZ'

db = SQLAlchemy(app)
app.app_context().push()

# LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(200), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)


db.create_all()

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('index.html',current_user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        new_user = User(username=form.email.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', form=form,current_user=current_user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    users = db.session.query(User).all()
    for user in users:
        if user.username == form.email.data and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html',form=form,current_user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create-checkout-session', methods=['GET','POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1M7htyCjDgYExzfYw9TAmbGk',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


if __name__ == '__main__':
    app.run(debug=True,port=4242)
