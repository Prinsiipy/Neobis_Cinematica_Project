# Generated by Django 4.2 on 2023-05-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_cinema_room_seat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='cinema',
        ),
        migrations.RemoveField(
            model_name='seat',
            name='room',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Cinema',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Seat',
        ),
    ]
