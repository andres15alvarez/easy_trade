from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StockConfig(AppConfig):
    name = "easy_trade.stock"
    verbose_name = _("Stock")
