# Generated by Django 4.2.1 on 2023-05-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StoreAPI", "0004_alter_product_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]
