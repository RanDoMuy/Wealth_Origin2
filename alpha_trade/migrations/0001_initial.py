# Generated by Django 4.1.6 on 2023-07-01 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=20)),
                ('trade_status', models.CharField(default='Active', max_length=50, verbose_name='Trade status')),
                ('trading_plan', models.CharField(default='No plan', max_length=50, verbose_name='Trading plan')),
                ('deposit_balance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Deposit_Balance')),
                ('profit_balance', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Profit Balance')),
                ('total_deposit', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Total Deposit')),
                ('total_withdrawal', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Total Withdrawal')),
                ('country', models.CharField(default='none', max_length=50, verbose_name='Country')),
                ('refcode', models.CharField(default='none', max_length=50, verbose_name='Ref Code')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
