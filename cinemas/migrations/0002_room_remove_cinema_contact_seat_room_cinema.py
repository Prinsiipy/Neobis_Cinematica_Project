# Generated by Django 4.2 on 2023-05-23 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='cinema',
            name='contact',
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.cinema'),
        ),
    ]