from controllers.card_controller import CardController
from controllers.user_controller import UserController
from controllers.transaction_controller import TransactionController

from schemas.transaction import Transaction
from schemas.card import Card

from datetime import datetime
from random import randint


def test_create_transaction():
    # Arrange
    user = UserController.create_user(RFC="JOJO70020384R2", CURP="JOJO700203", name="Jotaro Kujo",
                                      address="Tokyo, Japon",
                                      phone="123-123-1234", email="jojo3@hotmail.com", password="55555555")
    card = CardController.getcard(user=user, CLABE=1234567895214564, expiration_date=datetime(2024, 2, 1, 10, 10, 0),
                                  CVV=123, NIP=1234, credit_limit=50_000, credit_usage=0, balance=0)

    try:
        transaction = TransactionController.trans(card=card, reference=randint(1111111, 9999999),
                                                  concept="Army pants", amount=10_000,
                                                  transaction_date=datetime(2022, 2, 1, 10, 10, 0))

    except UnboundLocalError:
        print("Max credit limit reached")

    for u in Transaction.select():
        print(u.card.id, u.reference, u.concept, u.amount, u.transaction_date)

    for u in Card.select():
        print(u.credit_limit, u.credit_usage, u.balance)

    # Act
    created_transaction = Transaction.select().where(Transaction.id == transaction.id).get()

    # Assert
    assert transaction.id == created_transaction.id
    assert transaction.card == created_transaction.card
    assert transaction.reference == created_transaction.reference
    assert transaction.amount == created_transaction.amount
    assert transaction.transaction_date == created_transaction.transaction_date

    # Delete test instances
    card.delete_instance()
    user.delete_instance()
    created_transaction.delete_instance()


def test_create_fail_transaction():
    # Arrange
    user = UserController.create_user(RFC="JOJO70020384R2", CURP="JOJO700203", name="Jotaro Kujo",
                                      address="Tokyo, Japon",
                                      phone="123-123-1234", email="jojo3@hotmail.com", password="55555555")
    card = CardController.getcard(user=user, CLABE=1234567895214564, expiration_date=datetime(2024, 2, 1, 10, 10, 0),
                                  CVV=123, NIP=1234, credit_limit=50_000, credit_usage=0, balance=0)

    try:
        transaction = TransactionController.trans(card=card, reference=randint(1111111, 9999999),
                                                  concept="New phone", amount=60_000,
                                                  transaction_date=datetime(2022, 2, 1, 10, 10, 0))

    except UnboundLocalError:
        print("Max credit limit reached")

    for u in Transaction.select():
        assert isinstance(u.transaction_date, object)
        print(u.card.id, u.reference, u.concept, u.amount, u.transaction_date)

    for u in Card.select():
        assert isinstance(u.balance, object)
        print(u.credit_limit, u.credit_usage, u.balance)

    # Act
    created_transaction = Transaction.select().where(Transaction.id == transaction.id).get()

    # Assert
    assert transaction.id == created_transaction.id
    assert transaction.card == created_transaction.card
    assert transaction.reference == created_transaction.reference
    assert transaction.amount == created_transaction.amount
    assert transaction.transaction_date == created_transaction.transaction_date

    # Delete test instances
    card.delete_instance()
    user.delete_instance()
    created_transaction.delete_instance()




