from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.managers import CustomManager


class Users(AbstractUser):
    username = None
    last_name = None
    first_name = None

    class Role(models.TextChoices):
        PROJECT_OWNER = "Project Owner", _("Project Owner")
        PROJECT_MANAGER = "Project Manager", _("Project Manager")
        DEVELOPER = "Developer", _("Developer")
        TESTER = "Tester", _("Tester")

    email = models.EmailField(_("Email"), unique=True)
    role = models.CharField(_("Role"), max_length=20, choices=Role.choices, default=Role.PROJECT_OWNER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    objects = CustomManager()

    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        access = refresh.access_token
        return {
            "refresh": str(refresh),
            "access": str(access)
        }

    def __str__(self):
        return f"{self.email}"
