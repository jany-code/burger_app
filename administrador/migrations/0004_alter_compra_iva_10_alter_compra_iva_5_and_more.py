# Generated by Django 5.1.3 on 2025-04-06 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_alter_detallecompra_precio_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='iva_10',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='iva_5',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='monto_total',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total_iva',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='compra',
            name='total_sin_iva',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotal',
            field=models.BigIntegerField(),
        ),
    ]
