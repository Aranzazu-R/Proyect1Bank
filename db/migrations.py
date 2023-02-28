from peewee import SqliteDatabase

from schemas.user import User
from schemas.transaction import Transaction
from schemas.card import Card
from schemas.payment import Payment

db = SqliteDatabase('../proyect1.db')
db.create_tables([User, Transaction, Card, Payment])

# desde la teminal: from db.migrations import create_tables()
