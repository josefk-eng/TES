# Generated by Django 4.2.1 on 2023-06-02 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("StoreAPI", "0012_district_division_parish_village_street"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserToken",
            fields=[
                ("token", models.CharField(max_length=1000)),
                (
                    "deviceId",
                    models.CharField(max_length=500, primary_key=True, serialize=False),
                ),
                ("isActive", models.BooleanField(default=True)),
                ("address", models.CharField(default="", max_length=1000)),
                ("phoneNumber", models.CharField(default="", max_length=20)),
                ("name", models.CharField(default="", max_length=500)),
                ("email", models.CharField(default="", max_length=300)),
                ("password", models.CharField(default="", max_length=300)),
                ("dateAdded", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("price", models.IntegerField(default=0.0)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Placed", "Placed"),
                            ("Processed", "Processed"),
                            ("Delivered", "Delivered"),
                            ("Completed", "Completed"),
                        ],
                        default="Placed",
                        max_length=20,
                    ),
                ),
                ("items", models.CharField(default="", max_length=1000)),
                ("address", models.CharField(default="", max_length=1000)),
                ("contact", models.CharField(default="", max_length=1000)),
                ("contactName", models.CharField(default="", max_length=1000)),
                ("orderId", models.IntegerField(default=0)),
                ("remoteOrderId", models.IntegerField(default=0)),
                (
                    "identification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="StoreAPI.usertoken",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Order",
            },
        ),
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="StoreAPI.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="StoreAPI.product",
                    ),
                ),
            ],
            options={
                "unique_together": {("order", "product")},
            },
        ),
    ]
