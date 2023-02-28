from datetime import datetime
from schemas.user import User
from schemas.card import Card


class CardController:

    @staticmethod
    def getcard(user: User, CLABE: int, expiration_date: datetime, CVV: int, NIP: int, credit_limit: int,
                credit_usage: float, balance: float) -> Card:
        cc = Card(user=user.id, CLABE=CLABE, expiration_date=expiration_date,
                  CVV=CVV, NIP=NIP, credit_limit=credit_limit, credit_usage=credit_usage, balance=balance)
        cc.save()
        return cc

    # def get_available_credit(self):
    #    return self.credit_limit - self.credit_usage
