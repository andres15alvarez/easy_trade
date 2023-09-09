from django.db import models

from config.models import BaseControlModel, BaseModel
from easy_trade.user.models import User


class Stock(BaseModel):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=10)
    current_price = models.IntegerField(null=False)

    class Meta:
        db_table = "stock"


class HistoricalStock(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="prices")
    open = models.IntegerField(null=False)
    high = models.IntegerField(null=False)
    close = models.IntegerField(null=False)
    close = models.IntegerField(null=False)
    day = models.DateField()

    class Meta:
        db_table = "historical_stock"


class Wallet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets")
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="wallets")
    quantity = models.IntegerField()

    class Meta:
        db_table = "wallet"


class Transaction(BaseModel, BaseControlModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sales")
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="investments"
    )
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="wallets")
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = "transaction"
