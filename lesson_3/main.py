<<<<<<< HEAD
from flask import Flask, render_template, request
from models import db, User
from flask_wtf.csrf import CSRFProtect
from form_1 import LoginForms

app = Flask(__name__)
app.config['SECRET_KEY'] = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.secret_key = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'
csrf = CSRFProtect(app)
=======
import random

from flask import Flask, render_template
from models import db, Student, Faculty

app = Flask(__name__)
app.secret_key = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
>>>>>>> lesson_3
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


<<<<<<< HEAD
@app.route('/')
def index():
    return "Hi!"


@app.route('/login/', methods=['GET', 'POST'])
def register():
    form = LoginForms()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        user = User(
            firstname=form.email.data,
            surname=form.surname.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
    return render_template('login.html', form=form)
=======
@app.cli.command("test-data")
def add_test_data():
    count = 5
    for i in range(1, count + 1):
        faculty = Faculty(name=f"faculty{i}")
        db.session.add(faculty)
        for j in range(1, 3):
            student = Student(
                first_name=f"name{i}{j}",
                last_name=f"surname{i}{j}",
                age=random.randint(18, 25),
                group=2,
                gender=random.choice(["муж", "жен"]),
                faculty_id=i
            )
            db.session.add(student)
    db.session.commit()
    print('данные добавлены')


@app.route('/')
def all_users():
    students = Student.query.all()
    context = {'students': students}
    return render_template('users.html', **context)
>>>>>>> lesson_3


if __name__ == "__main__":
    app.run(debug=True)
