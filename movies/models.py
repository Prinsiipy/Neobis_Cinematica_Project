from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    is_active = models.BooleanField(default=True)

