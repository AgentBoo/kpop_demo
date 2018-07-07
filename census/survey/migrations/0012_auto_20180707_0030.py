# Generated by Django 2.0.5 on 2018-07-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20180703_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='age',
            field=models.CharField(choices=[('0-12', 'younger than 13'), ('13-17', '13-17'), ('18-24', '18-24'), ('25-34', '25-34'), ('35-44', '35-44'), ('45-54', '45-54'), ('55-64', '55-64'), ('65-200', '65+')], default='', max_length=20),
        ),
    ]
