# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их оценок.

from random import randint, choices

from flask import Flask, render_template
from bd_3 import db, Students, Ratings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task3.db'
db.init_app(app)


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем студентов
    for student in range(1, 6):
        new_student = Students(first_name=f'First name{student}', last_name=f'Last name{student}', group=randint(1, 10),
                               email=f'email{student}@mail.ru')
        db.session.add(new_student)
    db.session.commit()

    # Добавляем оценки
    for _ in range(1, 20):
        rates = Students.query.filter_by(first_name=f'First name{randint(1, 5)}').first()
        new_rate = Ratings(rates=rates, name=str(*choices(['Math', 'Phisics', 'Chemestry', 'English'])),
                           rating=randint(2, 5))
        db.session.add(new_rate)
    db.session.commit()


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
def print_rates():
    university = Students.query.all()
    ratings = Ratings.query.all()
    context = {'university': university,
               'ratings': ratings
               }
    return render_template('ratings_3.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
