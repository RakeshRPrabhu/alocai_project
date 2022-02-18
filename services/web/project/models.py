from project import db
from marshmallow import Schema, ValidationError, fields

class Game(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), unique= True, nullable= False)
    price = db.Column(db.Float(), nullable= False)
    space = db.Column(db.BigInteger, nullable= False)

    def __repr__(self):
        return '<Game - %r>' % self.name


# Validation Method
def must_not_be_negative(data):
    if data <= 0:
        raise ValidationError("Value cannot be negative")


# Game Schema
class GameSchema(Schema):
    name = fields.Str(required= True)
    price = fields.Float(required= True, validate = must_not_be_negative)
    space = fields.Int(required= True, validate = must_not_be_negative)

    class Meta:
        fields = ('name', 'price', 'space')
