# Generated by Django 4.2.1 on 2023-06-16 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("kisi", "0003_alter_kproduct_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="kreview",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="kisi.kproduct",
            ),
        ),
    ]