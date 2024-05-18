# Generated by Django 5.0.6 on 2024-05-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('fecha_visita', models.DateField()),
                ('hora_solicitud', models.TimeField(auto_now_add=True)),
                ('hora_visita', models.TimeField()),
            ],
        ),
    ]