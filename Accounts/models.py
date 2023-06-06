from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.utils.timezone import now
from . import managers
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta, timezone
from django.utils import timezone


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"
        CUSTOMER = "CUSTOMER", "Customer"

    base_role = Role.ADMIN
    role = models.CharField(max_length=50, choices=Role.choices)
    code = models.IntegerField(default=0)
    prev_code = models.IntegerField(default=0)
    expiry_date = models.DateTimeField('code expired', default=timezone.now())

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
        if self.code is not self.prev_code:
            dt = datetime.now()
            self.expiry_date = dt + timedelta(minutes=10)  # 10 minutes in the future
            self.prev_code = self.code
        return super().save(*args, **kwargs)


class Staff(User):
    base_role = User.Role.STAFF

    staff = managers.StaffManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(user=instance, staff_id=0)


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.IntegerField()


class Customer(User):
    base_role = User.Role.CUSTOMER

    customer = managers.CustomerManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.IntegerField(blank=True, null=True)
