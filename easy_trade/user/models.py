from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from config.models import BaseControlModel, BaseModel
from easy_trade.catalog.models import City, Country, Gender, UserType


class User(AbstractUser, BaseModel, BaseControlModel):
    """
    Default custom user model for easy_trade.
    """

    first_name = models.CharField(_("Name of User"), blank=True, max_length=255)
    last_name = models.CharField(_("Last name of User"), blank=True, max_length=255)
    date_of_birth = models.DateField(_("Date of birth of User"), blank=True)
    phone_number = models.CharField(
        _("Phone number of User"), blank=True, max_length=20
    )
    country_of_birth = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="users"
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="users")
    address = models.CharField(_("Address of User"), blank=True, max_length=255)
    zip_code = models.CharField(_("Zip code of User"), blank=True, max_length=7)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="users")
    type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name="users")

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("user:detail", kwargs={"username": self.username})
