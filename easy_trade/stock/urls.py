from django.urls import path

from easy_trade.stock.views import StockHistoricalView, StockView, WalletView

urlpatterns = [
    path("", StockView.as_view()),
    path("/historical", StockHistoricalView.as_view()),
    path("/wallet", WalletView.as_view()),
]
