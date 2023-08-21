# Задание №4
# Создайте форму регистрации пользователя с использованием Flask-WTF. Форма должна содержать следующие поля:
# ○ Имя пользователя (обязательное поле)
# ○ Электронная почта (обязательное поле, с валидацией на корректность ввода email)
# ○ Пароль (обязательное поле, с валидацией на минимальную длину пароля)
# ○ Подтверждение пароля (обязательное поле, с валидацией на совпадение с паролем)
# После отправки формы данные должны сохраняться в базе данных (можно использовать SQLite)
# и выводиться сообщение об успешной регистрации. Если какое-то из обязательных полей не
# заполнено или данные не прошли валидацию, то должно выводиться соответствующее сообщение об ошибке.
# Дополнительно: добавьте проверку на уникальность имени пользователя и электронной почты в
# базе данных. Если такой пользователь уже зарегистрирован, то должно выводиться сообщение об ошибке.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_4 import RegistrationForm
from bd_4 import db, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task4.db'
db.init_app(app)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        nickname = form.nickname.data
        email = form.email.data
        password = form.password.data
        if not Users.query.filter_by(nickname=nickname).first() and not \
                Users.query.filter_by(email=email).first():
            new_user = Users(nickname=nickname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('form_registration_4.html', form=form, succses=True)
        return render_template('form_registration_4.html', form=form, error=True)
    return render_template('form_registration_4.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
