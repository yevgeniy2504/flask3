import random

from flask import Flask, render_template
from models import db, Student, Faculty

app = Flask(__name__)
app.secret_key = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


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


if __name__ == "__main__":
    app.run(debug=True)
