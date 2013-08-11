from __future__ import unicode_literals
from django.db import models


class Artists(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'artists'


class Albums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artists)

    class Meta:
        db_table = 'albums'


class Tracks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Albums)
    path = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name + "(" + self.album.name + ")"

    class Meta:
        db_table = 'tracks'
