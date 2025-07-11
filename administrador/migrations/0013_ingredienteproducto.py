# Generated by Django 5.1.5 on 2025-05-06 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0012_alter_persona_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredienteProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, help_text='Cantidad usada en gramos(ej: 150) ', max_digits=10, verbose_name='cantidad en gramos')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.item', verbose_name='Ingrediente (Item)')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='administrador.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Ingrediente del producto',
                'unique_together': {('producto', 'item')},
            },
        ),
    ]
