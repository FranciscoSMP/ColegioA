# Generated by Django 5.0.3 on 2024-04-03 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstudiantesAutorizaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carne', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstudiantesPublicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carne', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('autoriza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiantesautorizaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Cometarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=500)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ManyToManyField(to='home.articulos')),
                ('comenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiantespublicaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.articulos')),
                ('publica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.estudiantespublicaciones')),
            ],
        ),
    ]