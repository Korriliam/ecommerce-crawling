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
    description = models.CharField(max_length=1048)
    ean = models.CharField(max_length=30)
    asin = models.CharField(max_length=30)
    brand = models.CharField(max_length=100)
    part_number = models.CharField(max_length=30)
    isbn = models.CharField(max_length=60)

    class Meta:
        db_table = "item"

class UserAgent(models.Model):
    """
    Some usual user agent used by the rotating user agent class
    of our app
    """
    user_agent = models.CharField(max_length=500)

    class Meta:
        db_table = "user_agent"


class Source(models.Model):
    """
     A source such as a marketplace
    """
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    language = models.CharField(max_length=15)

    class Meta:
        db_table = "source"


class Category(models.Model):
    """
    A category
    """
    name = models.CharField(max_length=255)
    source = models.ForeignKey(Source)
    class Meta:
        db_table = "category"


class Attribute(models.Model):
    """
     An item has some attributes aiming to describe it
    """
    name = models.CharField(max_length=255)


    class Meta:
        db_table = "attribute"


class ItemAttribute(models.Model):
    """

    """
    item = models.ForeignKey(Item)
    attribute = models.ForeignKey(Attribute)
    source = models.ForeignKey(Attribute)
    value = models.CharField(max_length=500)

    class Meta:
        db_table = "item_Attribute"

class ItemSource(models.Model):
    """

    """
    item = models.ForeignKey(Item)
    category = models.ForeignKey(Category)
    source = models.ForeignKey(Source)

    class Meta:
        db_table = "item_source"


