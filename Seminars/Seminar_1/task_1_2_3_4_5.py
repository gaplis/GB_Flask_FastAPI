# Задание1: Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
#
# Задание 2: Дорабатываем задачу 1.
# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about"
# страницу "contact".
#
# Задание 3: Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
#
# Задание 4: Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

# Задание 5: Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница"
# и абзацем "Привет, мир!".

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/sum/<int:num1>-<int:num2>')
def sum_num(num1, num2):
    return f'{num1} + {num2} = {num1 + num2}'


@app.route('/text/<text_str>')
def text(text_str):
    return f'Длина строки {text_str} = {len(text_str)}'


@app.route('/print/')
def print_html():
    html = """<h1>Моя первая HTML страница</h1><p>Привет, мир!</p>"""
    return html


if __name__ == '__main__':
    app.run(debug=True)
