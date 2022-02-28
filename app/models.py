# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Proxylist(models.Model):
    ip_address = models.CharField(max_length=255) 
    port = models.IntegerField(blank=True, null=True) 
    protocol = models.CharField(max_length=255, blank=True, null=True) 
    anonymity = models.CharField(max_length=255, blank=True, null=True) 
    country = models.CharField(max_length=255, blank=True, null=True) 
    region = models.CharField(max_length=255, blank=True, null=True) 
    city = models.CharField(max_length=255, blank=True, null=True) 
    uptime = models.FloatField(blank=True, null=True) 
    response = models.FloatField(blank=True, null=True) 
    transfer = models.FloatField(blank=True, null=True)
