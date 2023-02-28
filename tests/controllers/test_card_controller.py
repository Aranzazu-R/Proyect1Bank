from controllers.card_controller import CardController
from controllers.user_controller import UserController

from schemas.card import Card

from datetime import datetime
import pytest


def test_create_card():
    # Arrange
    user = UserController.create_user(RFC="JOJO70020384R2", CURP="JOJO700203", name="Jotaro Kujo",
                                      address="Tokyo, Japon",
                                      phone="123-123-1234", email="jojo3@hotmail.com", password="55555555")
    card = CardController.getcard(user=user, CLABE=1234567895214564, expiration_date=datetime(2024, 2, 1, 10, 10, 0),
                                  CVV=123, NIP=1234, credit_limit=50_000, credit_usage=0, balance=0)
    # Act
    created_card = Card.select().where(Card.id == card.id).get()

    # Assert
    assert card.id == created_card.id
    assert card.user == created_card.user
    assert card.CLABE == created_card.CLABE
    assert card.expiration_date == created_card.expiration_date
    assert card.CVV == created_card.CVV
    assert card.NIP == created_card.NIP
    assert card.credit_limit == created_card.credit_limit
    assert card.credit_usage == created_card.credit_usage
    assert card.balance == created_card.balance

    # Delete test instances
    created_card.delete_instance()
    user.delete_instance()
