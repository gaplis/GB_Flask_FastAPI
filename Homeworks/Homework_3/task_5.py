# Задание №5
# Создать форму регистрации для пользователя.
# Форма должна содержать поля: имя, электронная почта, пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# Валидация должна проверять, что все поля заполнены корректно
# (например, дата рождения должна быть в формате дд.мм.гггг).
# При успешной регистрации пользователь должен быть перенаправлен на страницу подтверждения регистрации.


from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_5 import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        return render_template('form_registration_5.html', form=form, succses=True)
    return render_template('form_registration_5.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
