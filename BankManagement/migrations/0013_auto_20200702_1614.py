# Generated by Django 3.0.7 on 2020-07-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankManagement', '0012_auto_20200702_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkaccount',
            name='CAccount_Balance',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='CAccount_Balance'),
        ),
    ]