from django.urls import path

from easy_trade.stock.views import StockView

urlpatterns = [
    path("", StockView.as_view()),
]
