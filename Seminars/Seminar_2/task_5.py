# Задача 5
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        opt = request.form.get('opt')
        match opt:
            case 'plus':
                res = num1 + num2
            case 'minus':
                res = num1 - num2
            case 'prod':
                res = num1 * num2
            case 'div':
                res = num1 / num2
        return render_template('calc_5.html', res=res)
    return render_template('calc_5.html', res=None)


if __name__ == '__main__':
    app.run(debug=True)
