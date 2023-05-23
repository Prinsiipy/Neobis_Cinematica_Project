from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Room(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Seat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)