# Generated by Django 4.2.5 on 2023-09-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas1', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fecha_nacimiento',
        ),
    ]
