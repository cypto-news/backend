# Generated by Django 4.0 on 2022-01-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_alter_market_price_alter_predict_prediction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='price',
            field=models.FloatField(),
        ),
    ]
