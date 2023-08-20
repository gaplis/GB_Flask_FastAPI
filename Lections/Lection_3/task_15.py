from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = b'f9c144fdddc88189b9abd1266538eb2ef0567a3f6f665779c691455758aae0bf'
csrf = CSRFProtect(app)
"""
Генерация надежного секретного ключа
>>> import secrets
>>> secrets.token_hex()
"""


@app.route('/')
def index():
    return 'Hi!'


@app.route('/form/', methods=['GET', 'POST'])
@csrf.exempt
def my_form():
    ...
    return 'No CSRF protection!'


if __name__ == '__main__':
    app.run(debug=True)
