from peewee import *
from schemas.card import Card

db = SqliteDatabase("proyect1.db")


class Payment(Model):
    card = ForeignKeyField(Card, backref="payments")
    amount = FloatField()
    concept = CharField(40)
    payment_date = DateTimeField()

    class Meta:
        database = db
