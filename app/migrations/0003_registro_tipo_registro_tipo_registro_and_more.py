# Generated by Django 4.1.6 on 2023-02-05 14:54

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_registro_begresos_alter_registro_bingresos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='tipo',
            field=models.CharField(choices=[('E', 'Egreso'), ('I', 'Ingreso')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='registro',
            name='tipo_registro',
            field=models.CharField(choices=[('EFE', 'Efectivo'), ('BAN', 'Banco')], default='EFE', max_length=3),
        ),
        migrations.AlterField(
            model_name='registro',
            name='begresos',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='registro',
            name='bingresos',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='registro',
            name='bsaldo',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='registro',
            name='eegresos',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='registro',
            name='eingresos',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
        migrations.AlterField(
            model_name='registro',
            name='esaldo',
            field=models.FloatField(blank=True, null=True, validators=[app.models.validate_even]),
        ),
    ]
