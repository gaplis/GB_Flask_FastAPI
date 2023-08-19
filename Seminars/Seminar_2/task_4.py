# Задача 4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/result/')
def result():
    context = {
        'txt': request.args.get('txt')
    }
    return render_template('result_4.html', **context)


@app.route('/text/', methods=['GET', 'POST'])
def text():
    if request.method == 'POST':
        txt = request.form.get('txt')
        res = str(len(txt.split()))
        return redirect(url_for('result', txt=res))
    return render_template('text_4.html')


if __name__ == '__main__':
    app.run(debug=True)
