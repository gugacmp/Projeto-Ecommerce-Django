# Generated by Django 4.2.3 on 2023-07-11 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='numero',
            field=models.DecimalField(decimal_places=10, max_digits=15, verbose_name='Numero '),
        ),
    ]