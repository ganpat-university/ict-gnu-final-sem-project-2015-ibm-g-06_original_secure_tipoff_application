# Generated by Django 4.1.5 on 2023-03-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("login_V1", "0002_delete_customuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="IPBlock",
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
                ("ip_address", models.GenericIPAddressField()),
                ("ip_range", models.CharField(max_length=100)),
            ],
        ),
    ]