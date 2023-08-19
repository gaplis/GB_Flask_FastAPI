# Задача 2
# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.

from pathlib import PurePath, Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_2.html')


@app.route('/another/', methods=['GET', 'POST'])
def another():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads', file_name))
        return f'Файл {file_name} загружен на сервер'
    return render_template('another_2.html')


if __name__ == '__main__':
    app.run(debug=True)
