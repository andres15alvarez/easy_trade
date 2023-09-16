from django.urls import path

from easy_trade.user.views import UserView

urlpatterns = [
    path("", UserView.as_view()),
]
