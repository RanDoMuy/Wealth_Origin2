# Generated by Django 4.1.6 on 2023-07-01 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpha_trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trade_status',
            field=models.CharField(default='Inactive', max_length=50, verbose_name='Trade status'),
        ),
    ]