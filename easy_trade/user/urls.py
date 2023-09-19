from django.urls import path

from easy_trade.user.views import CreateUserView, UserView

urlpatterns = [
    path("/create", CreateUserView.as_view()),
    path("", UserView.as_view()),
]
