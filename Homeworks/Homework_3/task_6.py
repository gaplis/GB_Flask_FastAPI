# Задание №6
# Дополняем прошлую задачу
# Создайте форму для регистрации пользователей в вашем веб-приложении.
# Форма должна содержать следующие поля: имя пользователя, электронная почта, пароль и подтверждение пароля.
# Все поля обязательны для заполнения, и электронная почта должна быть валидным адресом.
# После отправки формы, выведите успешное сообщение об успешной регистрации.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_6 import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return render_template('form_registration_6.html', form=form, succses=True)
    return render_template('form_registration_6.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
