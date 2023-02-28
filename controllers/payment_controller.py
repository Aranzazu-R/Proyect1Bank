from schemas.payment import Payment
from schemas.card import Card
from datetime import datetime


class PaymentController:

    @staticmethod
    def pay(card: Card, amount: float, concept: str, payment_date: datetime) -> Payment:
        if amount > 0:
            payment = Payment(card=card.id, amount=amount, concept=concept, payment_date=payment_date)
            payment.save()

            card.balance += amount
            card.credit_usage -= amount
            card.save()

        return payment
