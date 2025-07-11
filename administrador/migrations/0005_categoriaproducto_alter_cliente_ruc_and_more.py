# Generated by Django 5.1.5 on 2025-04-24 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0004_alter_compra_iva_10_alter_compra_iva_5_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categ', models.CharField(max_length=100, unique=True, verbose_name='Nombre de categoría')),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ruc',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='producto/', verbose_name='Imagen')),
                ('descripcion', models.TextField(blank=True, max_length=500, verbose_name='Descripción')),
                ('estado', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', max_length=1, verbose_name='Estado')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.categoriaproducto', verbose_name='Categoría')),
            ],
        ),
    ]
