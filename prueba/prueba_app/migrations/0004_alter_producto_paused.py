# Generated by Django 3.2.9 on 2021-11-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba_app', '0003_producto_paused'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='paused',
            field=models.BooleanField(),
        ),
    ]
