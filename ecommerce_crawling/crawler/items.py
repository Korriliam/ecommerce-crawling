from __future__ import unicode_literals
# -*- coding: utf8 -*-

# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from ecommerce_crawling.crawler.models import (
    Statistic, Item, UserAgent, ItemSource, ItemAttribute, Category, Source, Attribute
)

# All the following items are linked to a table in database (and to a scrapy model)


class UserAgentItem(DjangoItem):
    django_model = UserAgent

class ItemItem(DjangoItem):
    django_model = Item

class StatisticItem(DjangoItem):
    django_model = Statistic

class ItemAttributeItem(DjangoItem):
    django_model = ItemAttribute

class ItemSourceItem(DjangoItem):
    django_model = ItemSource

class CategoryItem(DjangoItem):
    django_model = Category

class SourceItem(DjangoItem):
    django_model = Source

class AttributeItem(DjangoItem):
    django_model = Attribute
