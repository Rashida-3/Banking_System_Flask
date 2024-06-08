from marshmallow import Schema, fields, validate


class TransactionSchema(Schema):
    transaction_id = fields.Int(dump_only=True)
    debit = fields.Float(allow_none=True, missing=None)
    credit = fields.Float(allow_none=True, missing=None)
    date = fields.Date(dump_only=True)
    time = fields.Time(dump_only=True) 
    account_balance = fields.Float(missing=0)
    user_id = fields.Int()

transaction_schema = TransactionSchema()
transaction_list_schema = TransactionSchema(many=True)