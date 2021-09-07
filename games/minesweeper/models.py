from django.db import models


# Create your models here.
class Minesweeper(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    cols = models.IntegerField()
    mines = models.IntegerField()
    player = models.CharField(max_length=255)
