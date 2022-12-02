from flask import Flask,request,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField
import datetime as dt
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'secret123@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class Task(FlaskForm):
    task = StringField('Write your next task here... ')
    date = DateField([InputRequired()])
    submit = SubmitField('Submit it here')

class DataBaseTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable= True)
    date = db.Column(db.String(250))

with app.app_context():
    db.create_all()


@app.route('/', methods= ['GET', 'POST'])
def home():
    form = Task()
    date_today = dt.date.today()
    if request.method == 'POST':
        print(form.date.data)
        new_task = DataBaseTask(task=form.task.data, date=form.date.data)
        db.session.add(new_task)
        db.session.commit()
    return render_template('index.html', form=form, date_today=date_today)

@app.route('/YourTodoList', methods=['POST', 'GET'])
def YourTodoList():
    all= db.session.query(DataBaseTask).all()
    return render_template('alltodos.html', all=all)

@app.route('/delete/<int:taskid>', methods=['GET','DELETE'])
def deletedb(taskid):
    delete= db.session.query(DataBaseTask).get(taskid)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
