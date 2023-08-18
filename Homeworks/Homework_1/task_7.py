# Задание №7
# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    _news = [{'news_title': 'Новость 3',
              'short_body': 'Краткое описание третьей новости...',
              'time_publish': '10 августа 2023 года'},
             {'news_title': 'Новость 2',
              'short_body': 'Краткое описание второй новости...',
              'time_publish': '5 августа 2023 года'},
             {'news_title': 'Новость 1',
              'short_body': 'Краткое описание первой новости...',
              'time_publish': '3 августа 2023 года'}, ]
    context = {'news': _news,
               'title': 'Задание 7: Вывод блока новостей', }
    return render_template('task_7.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
