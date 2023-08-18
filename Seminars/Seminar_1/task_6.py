# Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    sheet = [{'first_name': 'Илья',
                 'last_name': 'Чистов',
                 'age': '25',
                 'average': '4.6'},
                {'first_name': 'Екатерина',
                 'last_name': 'Князева',
                 'age': '24',
                 'average': '5.0'},
                {'first_name': 'Вячеслав',
                 'last_name': 'Пукач',
                 'age': '23',
                 'average': '4.3'},
                {'first_name': 'Светлана',
                 'last_name': 'Сушинская',
                 'age': '26',
                 'average': '5.0'}, ]
    sheet_head = list(sheet[0].keys())
    sheet_content = [list(i.values()) for i in sheet]
    return render_template('task_6.html', sheet_head=sheet_head, sheet_content=sheet_content)


if __name__ == '__main__':
    app.run(debug=True)
