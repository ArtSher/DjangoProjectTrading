# Generated by Django 4.1.6 on 2023-04-06 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0002_resumeuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGoods', models.CharField(max_length=70)),
                ('descriptionGoods', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('quantityGoods', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trading.goods')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trading.provider')),
            ],
        ),
    ]
