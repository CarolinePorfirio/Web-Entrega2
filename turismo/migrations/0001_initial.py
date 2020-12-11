# Generated by Django 2.2.16 on 2020-12-09 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('duration', models.CharField(max_length=100, verbose_name='Duracion')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('imag', models.ImageField(upload_to='packages', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizacion')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
            ],
            options={
                'verbose_name': 'Paquete',
                'verbose_name_plural': 'Paquetes',
                'ordering': ['-updated', '-created'],
            },
        ),
    ]