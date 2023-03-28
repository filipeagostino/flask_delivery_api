from marshmallow import Schema, fields

class deliverySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    cpf = fields.Str(required=True)
    phone = fields.Str(required=True)