# Задание №8
# Создать форму для регистрации пользователей на сайте.
# Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
# При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_8 import RegistrationForm
from bd_8 import db, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task8.db'
db.init_app(app)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        email = form.email.data
        new_user = Users(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template('form_registration_8.html', form=form, succses=True)
    return render_template('form_registration_8.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
