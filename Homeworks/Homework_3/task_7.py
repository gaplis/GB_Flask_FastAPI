# Задание №7
# Создайте форму регистрации пользователей в приложении Flask.
# Форма должна содержать поля: имя, фамилия, email, пароль и подтверждение пароля.
# При отправке формы данные должны валидироваться на следующие условия:
# ○ Все поля обязательны для заполнения.
# ○ Поле email должно быть валидным email адресом.
# ○ Поле пароль должно содержать не менее 8 символов, включая хотя бы одну букву и
# одну цифру.
# ○ Поле подтверждения пароля должно совпадать с полем пароля.
# ○ Если данные формы не прошли валидацию, на странице должна быть выведена
# соответствующая ошибка.
# ○ Если данные формы прошли валидацию, на странице должно быть выведено
# сообщение об успешной регистрации.

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_7 import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMS = '0123456789'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        password = form.password.data
        for letter in LETTERS:
            for num in NUMS:
                if letter in password and num in password:
                    return render_template('form_registration_7.html',
                                           form=form, succses='Вы успешно зарегистрировались!')
        return render_template('form_registration_7.html', form=form,
                               succses='В пароле должна быть хотя бы одна заглавная буква и одна цифра')
    return render_template('form_registration_7.html', form=form, succses=None)


if __name__ == '__main__':
    app.run(debug=True)
