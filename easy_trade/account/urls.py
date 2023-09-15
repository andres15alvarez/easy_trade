from django.urls import path

from easy_trade.account.views import AccountTransactionView, AccountView, CardView

urlpatterns = [
    path("", AccountView.as_view()),
    path("/transaction", AccountTransactionView.as_view()),
    path("/card", CardView.as_view()),
]
