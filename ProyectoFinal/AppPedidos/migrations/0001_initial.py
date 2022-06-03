# Generated by Django 4.0.4 on 2022-05-28 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=10)),
                ('Descripcion', models.CharField(max_length=40)),
                ('UnidadMedida', models.CharField(max_length=3)),
                ('Precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cuit', models.CharField(max_length=10)),
                ('RSocial', models.CharField(max_length=40)),
                ('Domicilio', models.CharField(max_length=40)),
                ('Mail', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
                ('Activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroPedido', models.IntegerField()),
                ('Articulo', models.CharField(max_length=10)),
                ('Cantidad', models.IntegerField()),
                ('Punitario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroPedido', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('CuitCliente', models.CharField(max_length=10)),
                ('Importe', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]