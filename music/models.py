from __future__ import unicode_literals
from django.db import models

class Artists(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255,unique=True) # This field type is a guess.
    class Meta:
        db_table = 'artists'

class Albums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255) # This field type is a guess.
    artist_id = models.ForeignKey(Artists)
    class Meta:
        db_table = 'albums'

class Tracks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255) # This field type is a guess.
    album_id = models.ForeignKey(Albums)
    length = models.IntegerField()
    class Meta:
        db_table = 'tracks'
