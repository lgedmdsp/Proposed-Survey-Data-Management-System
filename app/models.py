from __future__ import unicode_literals
from django.db import models

# Create your models here.


class data(models.Model):
    uniqueid = models.CharField(max_length=200, blank=True)
    eduid = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    upazilla = models.CharField(max_length=200, blank=True)
    s_union = models.CharField(max_length=200, blank=True)
    mouza = models.CharField(max_length=200, blank=True)
    village = models.CharField(max_length=200, blank=True)
    sheltername = models.CharField(max_length=200, blank=True)
    northing = models.FloatField(null=True, blank=True)
    easting = models.FloatField(null=True, blank=True)
    distance = models.FloatField(null=True, blank=True)
    expectedpopulation = models.FloatField(null=True, blank=True)
    waterlevel = models.FloatField(null=True, blank=True)
    pucca = models.FloatField(null=True, blank=True)
    semipucca = models.FloatField(null=True, blank=True)
    wooden = models.FloatField(null=True, blank=True)
    bamboo = models.FloatField(null=True, blank=True)
    thatched = models.FloatField(null=True, blank=True)
    shanty =models.FloatField(null=True, blank=True)
    total_house = models.FloatField(null=True, blank=True)

class district(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class upazilla(models.Model):
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Photo(models.Model):
    shelterid = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)