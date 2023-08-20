# Задание №1
# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
from random import randint, choices

from flask import Flask, render_template
from bd_1 import db, Students, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studentbase.db'
db.init_app(app)


@app.cli.command("fill-db")
def fill_tables():
    # Добавляем факультеты
    for fac in range(1, 6):
        new_fac = Faculty(fac_name=f'Fac{fac}')
        db.session.add(new_fac)
    db.session.commit()

    # Добавляем студентов
    for stud in range(1, 21):
        faculty = Faculty.query.filter_by(fac_name=f'Fac{randint(1, 5)}').first()
        new_student = Students(first_name=f'Name{stud}', last_name=f'Last name{stud}',
                               age=randint(18, 23), gender=str(*choices(['Male', 'Female'])),
                               group=randint(1, 10), faculty=faculty)
        db.session.add(new_student)
    db.session.commit()


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route("/")
def print_students():
    university = Students.query.all()
    context = {'university': university}
    return render_template('students_1.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
