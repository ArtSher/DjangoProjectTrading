# Generated by Django 4.1.6 on 2023-04-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_goods_provider_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='time_create',
            field=models.DateField(),
        ),
    ]
