# Generated by Django 5.1.7 on 2025-04-18 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_lojas_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clientes',
            new_name='empresa',
        ),
        migrations.CreateModel(
            name='dim_cliente',
            fields=[
                ('id_cliente', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('nome_cliente', models.CharField(max_length=100)),
                ('segmento', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=100)),
                ('regiao', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='dim_produto',
            fields=[
                ('id_produto', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('produto', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
                ('sub_categoria', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='dim_tempo_entrega',
            fields=[
                ('id_data_entrega', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('data_entrega', models.DateField()),
                ('dia_entrega', models.IntegerField()),
                ('mes_entrega', models.IntegerField()),
                ('ano_entrega', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='dim_tempo_venda',
            fields=[
                ('id_data_venda', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('data_venda', models.DateField()),
                ('dia_venda', models.IntegerField(editable=False)),
                ('mes_venda', models.IntegerField(editable=False)),
                ('ano_venda', models.IntegerField(editable=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='dim_tipo_entrega',
            fields=[
                ('id_tipo_entrega', models.CharField(primary_key=True, serialize=False, unique=True)),
                ('tipo_entrega', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
            ],
        ),
        
        migrations.CreateModel(
            name='fato_vendas',
            fields=[
                ('id_venda_item', models.CharField(primary_key=True, serialize=False, unique=True)),
                ('id_venda', models.CharField()),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('venda_valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('margem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('empresa', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.empresa')),
                ('id_cliente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.dim_cliente')),
                ('id_data_entrega', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.dim_tempo_entrega')),
                ('id_data_venda', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.dim_tempo_venda')),
                ('id_produto', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.dim_produto')),
                ('id_tipo_entrega', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='api.dim_tipo_entrega')),
            ],
        ),
        migrations.DeleteModel(
            name='lojas',
        ),
    ]
