# Generated by Django 3.2.7 on 2022-01-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_V1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]