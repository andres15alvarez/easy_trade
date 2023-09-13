from django.urls import path

from easy_trade.stock.views import StockHistoricalView, StockView

urlpatterns = [
    path("", StockView.as_view()),
    path("/historical", StockHistoricalView.as_view()),
]
