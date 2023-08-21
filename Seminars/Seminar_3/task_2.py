# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

from random import randint

from flask import Flask, render_template
from bd_2 import db, Authors, Books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booksbase.db'
db.init_app(app)


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем авторов
    for auth in range(1, 4):
        new_auth = Authors(first_name=f'First name{auth}', last_name=f'Last name{auth}')
        db.session.add(new_auth)
    db.session.commit()

    # Добавляем книги
    for book in range(1, 11):
        author = Authors.query.filter_by(first_name=f'First name{randint(1, 3)}').first()
        new_book = Books(name=f'Name{book}', year=randint(1800, 2000),
                         count=randint(10000, 1000000), author=author)
        db.session.add(new_book)
    db.session.commit()


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
def print_books():
    library = Books.query.all()
    context = {'library': library}
    return render_template('library_2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
