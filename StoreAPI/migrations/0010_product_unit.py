# Generated by Django 4.2.1 on 2023-05-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("StoreAPI", "0009_product_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="unit",
            field=models.CharField(default="Kgs", max_length=50),
        ),
    ]