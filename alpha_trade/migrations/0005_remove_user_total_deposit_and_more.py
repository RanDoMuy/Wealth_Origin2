# Generated by Django 4.1.6 on 2023-07-01 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alpha_trade', '0004_alter_deposit_history_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='total_deposit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='total_withdrawal',
        ),
    ]