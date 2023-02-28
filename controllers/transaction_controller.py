from schemas.transaction import Transaction
from schemas.card import Card
from datetime import datetime


class TransactionController:

    @staticmethod
    def trans(card: Card, reference: int, concept: str, amount: float,
              transaction_date: datetime) -> Transaction:

        if (card.credit_limit - card.credit_usage) >= amount:
            trans = Transaction(card=card.id, reference=reference, concept=concept, amount=amount,
                                transaction_date=transaction_date)
            trans.save()

            card.balance -= amount
            card.credit_usage += amount
            card.save()
        else:
            raise ValueError("Max ...")

        return trans
