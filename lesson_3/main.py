from flask import Flask, render_template, request
from models import db, User
from flask_wtf.csrf import CSRFProtect
from form_1 import LoginForms

app = Flask(__name__)
app.config['SECRET_KEY'] = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.secret_key = b'1b3c677c38cd835d77f1fa821ea055d53e884c70f20ca783a9e44b63e0492453'
csrf = CSRFProtect(app)
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


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


if __name__ == "__main__":
    app.run(debug=True)
