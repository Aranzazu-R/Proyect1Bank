from peewee import * 
from schemas.card import Card


db = SqliteDatabase("proyect1.db")


class Transaction(Model):
    card = ForeignKeyField(Card, backref='transactions')
    reference = IntegerField(7)
    concept = CharField(40)
    amount = FloatField()
    transaction_date = DateTimeField()

    class Meta:
        database = db