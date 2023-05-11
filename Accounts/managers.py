from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _
from . import models


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=models.User.Role.STAFF)


class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=models.User.Role.CUSTOMER)
