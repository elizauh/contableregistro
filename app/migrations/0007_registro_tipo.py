# Generated by Django 4.1.6 on 2023-02-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_registro_btotalegresos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='tipo',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Banco', 'Banco')], default='Efectivo', max_length=200),
        ),
    ]
