from marshmallow import Schema, fields, validate



class user_schema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email()
    password = fields.String(required=True, validate=validate.Length(min=8))
    balance = fields.Float(missing=0)
    is_admin = fields.Boolean(missing=False,required=False)
    pin = fields.Integer(required=True, validate=lambda x: len(str(x)) == 4,error_messages={'validator_failed': 'PIN must be a 4-digit number'})
    account_no = fields.Integer(required=False)

userschema = user_schema()
user_list_schema = user_schema(many=True)