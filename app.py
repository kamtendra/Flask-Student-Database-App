from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Change this to your database URI
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    college = db.Column(db.String(100))
    roll = db.Column(db.Integer)
    branch = db.Column(db.String(100))

    def __init__(self, name, college, roll, branch):
        self.name = name
        self.college = college
        self.roll = roll
        self.branch = branch


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        roll = request.form['roll']
        branch = request.form['branch']

        student = Student(name=name, college=college, roll=roll, branch=branch)
        db.session.add(student)
        db.session.commit()

    students = Student.query.all()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
