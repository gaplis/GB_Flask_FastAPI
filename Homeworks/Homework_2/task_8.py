# Задание №8
# Создать страницу, на которой будет форма для ввода имени и кнопка "Отправить"
# При нажатии на кнопку будет произведено перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

from flask import Flask, flash, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = b'deafaeef311c699ce881889884dfedb58ae6563429dea620d3be2c69a6f958db'


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        name = request.form.get('name')
        flash(f'Привет, {name}', 'success')
        return redirect(url_for('main'))
    return render_template('main_8.html')


if __name__ == '__main__':
    app.run(debug=True)
