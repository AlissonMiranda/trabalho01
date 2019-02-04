# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-02 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataFesta', models.DateField(verbose_name='Data da festa')),
                ('horaInicio', models.TimeField(verbose_name='Hora de inicio')),
                ('horaTermino', models.TimeField(verbose_name='Hora termino')),
                ('valorCobrado', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor cobrado')),
            ],
            options={
                'verbose_name': 'aluguel',
                'verbose_name_plural': 'Alugueis',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.DateField()),
                ('telefone', models.TimeField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Endere\xe7o')),
                ('numero', models.CharField(max_length=50, verbose_name='N')),
                ('complemento', models.CharField(max_length=150, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=50, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=20, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'Endere\xe7o',
                'verbose_name_plural': 'Endere\xe7os',
            },
        ),
        migrations.CreateModel(
            name='ItemTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Itens de Temas',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('valorAluguel', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor do aluguel')),
                ('corToalha', models.CharField(max_length=100, verbose_name='Cor da toalha')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
    ]
