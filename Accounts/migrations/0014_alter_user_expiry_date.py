# Generated by Django 4.2.1 on 2023-05-31 11:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0013_alter_user_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 5, 31, 11, 9, 59, 459515, tzinfo=datetime.timezone.utc
                ),
                verbose_name="code expired",
            ),
        ),
    ]