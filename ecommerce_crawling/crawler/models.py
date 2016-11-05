from __future__ import unicode_literals
# -*- coding: utf8 -*-

from django.db import models



class Statistic(models.Model):
    '''
    Contains the stats attached to each crawling operation/session (nb of results, ...)
    '''
    startTime = models.DateTimeField()
    finishTime = models.DateTimeField()
    finishReason = models.CharField(max_length=200)
    requestBytes = models.BigIntegerField()
    responseBytes = models.BigIntegerField()
    requestCount = models.BigIntegerField()
    responseCount = models.BigIntegerField()
    responseReceivedCount = models.BigIntegerField()
    requestDepthMax = models.IntegerField()
    requestStatusCount200 = models.BigIntegerField()
    requestStatusCount301 = models.BigIntegerField()
    requestStatusCount302 = models.BigIntegerField()
    requestStatusCount500 = models.BigIntegerField()
    requestStatusCount404 = models.BigIntegerField()
    dupeFiltered = models.BigIntegerField()
    imgCount = models.BigIntegerField()
    nbScrapedItems = models.BigIntegerField()

    class Meta:
        db_table = "statistic"

class Item(models.Model):
    """
    A single item
    """
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    marketplace_name = models.CharField(max_length=255)

    class Meta:
        db_table = "item"

class UserAgent(models.Model):
    user_agent = models.CharField(max_length=500)

    class Meta:
        db_table = "user_agent"
