from flask import Flask,request,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_user,logout_user,current_user,LoginManager
from forms import LoginForm,RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.secret_key='supersecretkey123@'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String,unique=True,nullable=False)
    password=db.Column(db.String, nullable=False)
app.app_context().push()
db.create_all()

@app.route('/')
def home():
    return render_template('index.html',current_user=current_user)

@app.route('/about')
def about():
    return render_template('about.html',current_user=current_user)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password.data
        user=User.query.filter_by(email=email).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html',current_user=current_user,form=form)

@app.route('/projects')
def projects():
    return render_template('projects.html',current_user=current_user)

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if request.method == 'POST':
        user = User(email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',current_user=current_user,form=form)

@app.route('/upload')
def upload():
    return render_template('upload.html',current_user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

