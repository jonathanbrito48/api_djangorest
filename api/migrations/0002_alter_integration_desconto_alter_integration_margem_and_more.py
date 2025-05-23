# Generated by Django 5.1.7 on 2025-04-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integration',
            name='desconto',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='integration',
            name='margem',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='integration',
            name='quantidade_vendida',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='integration',
            name='valor_venda',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
