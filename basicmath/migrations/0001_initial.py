# Generated by Django 5.0.6 on 2024-09-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SumaPrimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.IntegerField(help_text='Ingresa el valor de n')),
                ('suma_primos', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
