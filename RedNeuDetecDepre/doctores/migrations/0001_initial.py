# Generated by Django 3.0.8 on 2021-01-09 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('birth_date', models.DateTimeField(auto_now_add=True)),
                ('sex', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('study', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('civil_state', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('economical_situation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Beck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tristeza', models.IntegerField()),
                ('pesimismo', models.IntegerField()),
                ('fracaso', models.IntegerField()),
                ('placer', models.IntegerField()),
                ('culpa', models.IntegerField()),
                ('castigo', models.IntegerField()),
                ('disconformidad', models.IntegerField()),
                ('autocritica', models.IntegerField()),
                ('llanto', models.IntegerField()),
                ('agitacion', models.IntegerField()),
                ('interes', models.IntegerField()),
                ('indecision', models.IntegerField()),
                ('desvalorizacion', models.IntegerField()),
                ('energia', models.IntegerField()),
                ('sueño', models.IntegerField()),
                ('irritabilidad', models.IntegerField()),
                ('apetito', models.IntegerField()),
                ('concentracion', models.IntegerField()),
                ('fatiga', models.IntegerField()),
                ('sexo', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctores.Paciente')),
            ],
        ),
    ]
