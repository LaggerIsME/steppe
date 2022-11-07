from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String(200), nullable=False)
    password = db.Column(String(200), nullable=False)
