from django.db import models

from config.models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "country"


class State(BaseModel):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="states"
    )

    class Meta:
        db_table = "state"


class City(BaseModel):
    name = models.CharField(max_length=150)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities")

    class Meta:
        db_table = "city"


class Document(BaseModel):
    document_type = models.CharField(max_length=150)

    class Meta:
        db_table = "document"


class Gender(BaseModel):
    name = models.CharField(max_length=150)

    class Meta:
        db_table = "gender"


class UserType(BaseModel):
    type = models.CharField(max_length=150)

    class Meta:
        db_table = "user_type"
