# Generated by Django 5.1.2 on 2024-10-11 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_payme", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="balance",
            old_name="order_id",
            new_name="user_id",
        ),
    ]
