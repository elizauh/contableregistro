# Generated by Django 4.1.6 on 2023-02-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_registro_tipo_registro_tipo_registro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='tipo_registro',
        ),
    ]
