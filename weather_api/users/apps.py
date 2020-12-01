from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "weather_api.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import weather_api.users.signals  # noqa F401
        except ImportError:
            pass
