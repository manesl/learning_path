from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(64), index = True)
    code = db.Column(db.String(64), index = True, unique = True)
    lessons = db.relationship('Lessons', backref='course', lazy = 'dynamic')


    def __repr__(self):
        return '{}'.format(self.title)

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    link = db.Column(db.String(64))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    def __repr__(self):
        return '<Lesson: {}>'.format(self.title)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))