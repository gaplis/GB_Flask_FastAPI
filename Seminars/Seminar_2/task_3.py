# Задача 3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и
# переход на страницу приветствия пользователя или страницу с ошибкой.


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/hello/')
def hello_page(name=None):
    context = {
        'name': name or 'Ilya'
    }
    return render_template('hello_1.html', **context)


@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == 'Ilya' and password == 'pass':
            return redirect(url_for('hello_page', name=name))
        return render_template('form_page_3.html', error=True)
    return render_template('form_page_3.html', error=None)


if __name__ == '__main__':
    app.run(debug=True)
