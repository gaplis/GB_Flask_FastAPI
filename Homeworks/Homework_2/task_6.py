# Задание №6
# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        res = int(request.form.get('age'))
        if res < 14:
            abort(404)
        return redirect(url_for('result', age=res))
    return render_template('main_6.html')


@app.route('/result/')
def result():
    context = {
        'age': request.args.get('age')
    }
    return render_template('result_6.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Неверное значение возраста',
        'url': request.base_url,
    }
    return render_template('404_6.html', **context), 404


if __name__ == '__main__':
    app.run(debug=True)
