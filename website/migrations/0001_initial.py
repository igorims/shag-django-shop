# Generated by Django 3.2.7 on 2021-09-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название продукта)')),
                ('description', models.TextField(verbose_name='Описание продукта')),
                ('price', models.IntegerField(verbose_name='Цена продукта')),
            ],
        ),
    ]
