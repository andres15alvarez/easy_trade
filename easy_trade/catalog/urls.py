from django.urls import path

from easy_trade.catalog.views import (
    CityView,
    CountryView,
    DocumentView,
    GenderView,
    StateView,
    UserTypeView,
)

urlpatterns = [
    path("/country", CountryView.as_view()),
    path("/state", StateView.as_view()),
    path("/city", CityView.as_view()),
    path("/document", DocumentView.as_view()),
    path("/gender", GenderView.as_view()),
    path("/usertype", UserTypeView.as_view()),
]
