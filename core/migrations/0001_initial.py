# Generated by Django 4.2.3 on 2023-07-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnome', models.CharField(max_length=100, verbose_name='Primeiro Nome : ')),
                ('snome', models.CharField(max_length=80, verbose_name='Segundo Nome : ')),
                ('email', models.EmailField(max_length=100, verbose_name='Email : ')),
                ('sexo', models.CharField(max_length=1, verbose_name='Sexo : ')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartao', models.CharField(max_length=100, verbose_name='Cartão :')),
                ('numero', models.DecimalField(decimal_places=4, max_digits=9, verbose_name='Numero : ')),
                ('bandeira', models.CharField(max_length=50, verbose_name='Bandeira : ')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome ')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preco ')),
                ('estoque', models.IntegerField(verbose_name='Qnt Produto')),
            ],
        ),
    ]
