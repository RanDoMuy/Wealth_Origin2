# Generated by Django 4.1.6 on 2023-07-02 00:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alpha_trade', '0010_rename_date_deposit_history_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdrawal_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit Balance')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.CharField(blank=True, max_length=50, verbose_name='Deposit Status')),
                ('address', models.CharField(blank=True, max_length=70, verbose_name='Wallet Address')),
                ('method', models.CharField(blank=True, max_length=50, verbose_name='Deposit Method')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]