from django.db import models

from config.models import BaseControlModel, BaseModel
from easy_trade.user.models import User


class Account(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account")
    balance = models.IntegerField()

    class Meta:
        db_table = "account"


class Card(BaseControlModel, BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    number = models.CharField(max_length=16)
    exp_date = models.DateField()
    cvv = models.CharField(max_length=3)
    name_on_card = models.CharField(max_length=100)

    class Meta:
        db_table = "card"


class AccountTransaction(BaseModel, BaseControlModel):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="transactions"
    )
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE, related_name="transactions"
    )
    type = models.CharField(max_length=10)
    amount = models.IntegerField()

    class Meta:
        db_table = "account_transaction"
