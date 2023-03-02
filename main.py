from db import migrations

from controllers.transaction_controller import TransactionController
from controllers.card_controller import CardController
from controllers.user_controller import UserController
from controllers.payment_controller import PaymentController

from schemas.card import Card
from schemas.transaction import Transaction
from schemas.user import User
from schemas.payment import Payment
from datetime import datetime

from db import migrations

from random import randint

# Simulación Usuarios

user = UserController.create_user(
    RFC='MOMM991110BQ3',
    CURP='MOMM991110',
    name='Miguel Moreno',
    address='Contadores 597',
    phone=3334882893,
    email='if722133@iteso.mx',
    password='contrasena')
user.save()

print("Este es el usuario:")

for u in User.select():
    print(u.id, u.RFC, u.CURP, u.name, u.address)

# Simulation Cards

migue1 = User.select().where(User.id == 1).get()

card = CardController.getcard(user=migue1, CLABE=1234567895214564, expiration_date=datetime(2023, 2, 1, 10, 10, 0),
                              CVV=521, NIP=2196, credit_limit=49_000, credit_usage=0, balance=0)

print("Esta es la tarjeta del usuario:")

for u in Card.select():
    print(u.user.id, u.CLABE, u.expiration_date, u.CVV, u.NIP, u.credit_limit, u.credit_usage, u.balance)

# Simulation Transactions

migue_card = Card.select().where(Card.id == 1).get()

try:
    transaccion_sim = TransactionController.trans(card=migue_card, reference=randint(1111111, 9999999),
                                                  concept='Boletos Fórmula 1', amount=20_000,
                                                  transaction_date=datetime(2021, 2, 1, 10, 10, 0))

except ValueError:
    print("Max credit limit reached")

print("Esta es la transaccion (compra):")
for u in Transaction.select():
    print(u.card.id, u.reference, u.concept, u.amount, u.transaction_date)

print("Este es el balance de la cuenta despues de la transaccion:")
# Regresar el balance de la cuenta
for u in Card.select():
    print(u.credit_limit, u.credit_usage, u.balance)

# Simulation payment

migue_pay = Card.select().where(Card.id == 1).get()

payment_sim = PaymentController.pay(card=migue_pay, amount=10_000, concept="Pago tarjeta",
                                    payment_date=datetime(2023, 2, 23, 10, 10, 0))

print("Este es el pago a la cuenta:")
for u in Payment.select():
    print(u.card.id, u.amount, u.concept, u.payment_date)

print("Este es el balance de la cuenta despues del pago:")
for u in Card.select():
    print(u.credit_limit, u.credit_usage, u.balance)

Card.delete().execute()
Payment.delete().execute()
User.delete().execute()
Transaction.delete().execute()
