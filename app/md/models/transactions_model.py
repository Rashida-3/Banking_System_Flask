from app import db

class Transaction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    credit = db.Column(db.Float,nullable=True)
    debit = db.Column(db.Float,nullable=True)
    date = db.Column(db.Date,nullable=False)
    time = db.Column(db.Time,nullable=False)
    account_balance = db.Column(db.Float,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    transaction_id = db.Column(db.Integer,nullable=False,unique=True)
    