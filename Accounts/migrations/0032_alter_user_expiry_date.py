# Generated by Django 4.2.1 on 2023-06-16 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0031_alter_user_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="expiry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 16, 10, 48, 42, 640452, tzinfo=datetime.timezone.utc
                ),
                verbose_name="code expired",
            ),
        ),
    ]
