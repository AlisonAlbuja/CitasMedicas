from marshmallow import Schema, fields

class EditUserSchema(Schema):
    username = fields.String(required=False)
    email = fields.Email(required=False)
