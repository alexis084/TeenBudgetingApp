# from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

class User(db.Model, UserMixin):
    username = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    checkingBalance = db.Column(db.Float, unique=False, nullable=False, default=0.00)
    savingBalance = db.Column(db.Float, unique=False, nullable=False, default=0.00)
    #savingPercent = db.Column(db.Float, unique=False, nullable=False, default=0.00)

    def get_id(self):
        return self.username

    def __repr__(self):
        return f"Username: '{self.username}, Checking Balance:'{self.checkingBalance}', Saving Balance:'{self.savingBalance}'"


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    date = db.Column(db.String(20), unique=False, nullable=False)
    purpose = db.Column(db.String(20), unique=False, nullable=False, default='withdrawal')
    amount = db.Column(db.Float, unique=False, nullable=False, default=0.00)
    category = db.Column(db.String(20), unique=False, nullable=True)
    savingPercent = db.Column(db.Float, unique=False, nullable=True, default=0.00) #changed nullable to True


    def __repr__(self):
        return f"'{self.username}'|'{self.date}'|'{self.purpose}'|'{self.amount}'|'{self.category}'"