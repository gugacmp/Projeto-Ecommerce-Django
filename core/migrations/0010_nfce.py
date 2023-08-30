# Generated by Django 4.2.3 on 2023-08-04 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_vender_nfe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nfce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('cores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cores')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fornecedor')),
                ('pagamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pagamento')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.produto')),
                ('tributacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tributacao')),
                ('vendas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vender')),
            ],
        ),
    ]