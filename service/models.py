# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Playlist(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50)
    videos = models.TextField(default='')