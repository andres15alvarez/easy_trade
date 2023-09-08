from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "easy_trade.users"
    verbose_name = _("Users")
