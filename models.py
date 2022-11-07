from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(200), nullable=False, unique = True)
    password = db.Column(String(200), nullable=False)
    first_name = db.Column(String(200), nullable=False)
    second_name = db.Column(String(200), nullable=False)
    country = db.Column(String(200), nullable=False)
    date_of_birth = db.Column(Date, nullable=False)



