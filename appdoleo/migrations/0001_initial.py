# Generated by Django 3.2.13 on 2023-09-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('participa', models.IntegerField()),
                ('vitorias', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenistas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('patrocinio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Torneios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('nomeTorneio', models.CharField(max_length=50)),
                ('nomeJogador', models.CharField(max_length=50)),
                ('vitorias', models.IntegerField()),
            ],
        ),
    ]
