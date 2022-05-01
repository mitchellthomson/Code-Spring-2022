from enum import unique
from flask_login import UserMixin

from sqlalchemy.sql import func
from . import db


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    psw = db.Column(db.String(150))
    
    notes = db.relationship("Note")