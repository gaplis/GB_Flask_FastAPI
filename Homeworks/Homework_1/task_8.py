# Задание №8
# Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для каждой отдельной страницы.
# Например, создать страницу "О нас" и "Контакты", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {"title": 'Главная'}
    return render_template('task_8_main.html', **context)


@app.route('/about/')
def about():
    context = {"title": 'О сайте'}
    return render_template('task_8_about.html', **context)


@app.route('/contacts/')
def contacts():
    _contact = [{'who': 'Создатель сайта',
                 'name': 'Илья Чистов',
                 'tg': '@gaplis'},
                {'who': 'Моя кошка',
                 'name': 'Киви',
                 'tg': '@very_cute_kitty'}, ]
    context = {"title": 'Контакты',
               'contact': _contact}
    return render_template('task_8_contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
