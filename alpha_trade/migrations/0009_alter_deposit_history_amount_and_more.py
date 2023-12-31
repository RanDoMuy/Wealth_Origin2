# Generated by Django 4.1.6 on 2023-07-01 23:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha_trade', '0008_deposit_history_investment_plan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit_history',
            name='amount',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit Balance'),
        ),
        migrations.AlterField(
            model_name='deposit_history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='deposit_history',
            name='method',
            field=models.CharField(blank=True, max_length=50, verbose_name='Deposit Method'),
        ),
        migrations.AlterField(
            model_name='deposit_history',
            name='status',
            field=models.CharField(blank=True, max_length=50, verbose_name='Deposit Status'),
        ),
    ]
