# Задание №9
# Создать страницу, на которой будет форма для ввода имени и электронной почты
# При отправке которой будет создан cookie файл с данными пользователя
# Также будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.

from flask import Flask, flash, redirect, url_for, request, render_template, session, make_response

app = Flask(__name__)
app.secret_key = b'deafaeef311c699ce881889884dfedb58ae6563429dea620d3be2c69a6f958db'


@app.route('/')
def main():
    if 'username' in session:
        return render_template('main_9.html', username=session["username"])
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        # response = make_response()
        # response.set_cookie('username', request.form.get('username'))
        # response.set_cookie('mail', request.form.get('mail'))
        return redirect(url_for('main'))
    return render_template('login_9.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    print('Удалили сессию')
    # make_response().delete_cookie('username')
    # make_response().delete_cookie('mail')
    # request.cookies.pop('username')
    # request.cookies.pop('mail')
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
