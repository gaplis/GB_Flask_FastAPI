# Задание №9
# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна
# (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {"title": 'Главная'}
    return render_template('task_9_main.html', **context)


@app.route('/outerwear/')
def outerwear():
    context = {"title": 'Нижняя одежда'}
    return render_template('task_9_outerwear.html', **context)


@app.route('/underwear/')
def underwear():
    context = {"title": 'Верхняя одежда'}
    return render_template('task_9_underwear.html', **context)


@app.route('/shoes/')
def shoes():
    context = {"title": 'Обувь'}
    return render_template('task_9_shoes.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
