from __future__ import unicode_literals
from django.db import models

class Albums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField() # This field type is a guess.
    artist_id = models.IntegerField()
    class Meta:
        db_table = 'albums'

class Artists(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True) # This field type is a guess.
    class Meta:
        db_table = 'artists'

class Tracks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField() # This field type is a guess.
    album_id = models.IntegerField()
    length = models.IntegerField()
    class Meta:
        db_table = 'tracks'
