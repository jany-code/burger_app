# Generated by Django 5.1.5 on 2025-05-19 01:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administrador', '0014_alter_item_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timbrado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20, unique=True, verbose_name='Numero de timbrado')),
                ('ruc', models.CharField(max_length=20, verbose_name='Ruc del emisor')),
                ('fecha_inicio_vigencia', models.DateField(verbose_name='Inicio de vigencia')),
                ('fecha_fin_vigencia', models.DateField(verbose_name='Fin de Vigencia')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('cod_fact', models.AutoField(primary_key=True, serialize=False)),
                ('nro_fact', models.CharField(max_length=20, unique=True)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('direccion_cliente', models.CharField(max_length=200)),
                ('telefono_cliente', models.CharField(max_length=20)),
                ('ruc_cliente', models.CharField(max_length=20)),
                ('subtotal', models.BigIntegerField(default=0)),
                ('iva_10', models.BigIntegerField(default=0)),
                ('total_iva', models.BigIntegerField(default=0)),
                ('monto_total', models.BigIntegerField(default=0)),
                ('descuento', models.BigIntegerField(default=0)),
                ('forma_de_pago', models.CharField(choices=[('EFECTIVO', 'Efectivo')], default='EFECTIVO', max_length=20)),
                ('fecha_emision', models.DateField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='facturas', to='administrador.cliente')),
                ('timbrado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturacion.timbrado')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('cod_det_fact', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=255)),
                ('codigo_producto', models.CharField(max_length=20)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.PositiveIntegerField()),
                ('descuento', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('total', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administrador.producto')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='facturacion.factura')),
            ],
        ),
    ]
