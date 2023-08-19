from flask import Flask, flash, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = b'deafaeef311c699ce881889884dfedb58ae6563429dea620d3be2c69a6f958db'
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ == '__main__':
    app.run(debug=True)
