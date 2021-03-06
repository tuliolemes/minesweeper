# Generated by Django 3.2.7 on 2021-09-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minesweeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rows', models.IntegerField()),
                ('cols', models.IntegerField()),
                ('mines', models.IntegerField()),
                ('player', models.CharField(max_length=255)),
            ],
        ),
    ]
