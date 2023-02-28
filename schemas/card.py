from peewee import *
from peewee import FloatField

from schemas.user import User

db = SqliteDatabase("proyect1.db")


class Card(Model):
    user = ForeignKeyField(User, backref="cards")
    CLABE = IntegerField()
    expiration_date = DateField()
    CVV = IntegerField(3)
    NIP = IntegerField(4)
    credit_limit = FloatField()
    credit_usage = FloatField()
    balance: FloatField = FloatField()

    class Meta:
        database = db
