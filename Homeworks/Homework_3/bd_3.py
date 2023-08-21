from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}'


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    rating_id = db.relationship('Ratings', backref='rates', lazy=True)
