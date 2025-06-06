# Generated by Django 5.0.2 on 2025-05-23 18:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_clase_options_alter_reserva_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clase',
            options={},
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={},
        ),
        migrations.RemoveField(
            model_name='clase',
            name='instructor',
        ),
        migrations.RemoveField(
            model_name='clase',
            name='sala',
        ),
        migrations.AlterField(
            model_name='clase',
            name='cupos_disponibles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clase',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='clase',
            name='horario',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='clase',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.clase'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
