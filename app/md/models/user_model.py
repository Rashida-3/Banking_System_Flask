from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    balance = db.Column(db.Float,default=0)
    pin = db.Column(db.Integer,nullable=False)
    account_no = db.Column(db.Integer,nullable=False,unique=True)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

from app.md.models.transactions_model import Transaction
