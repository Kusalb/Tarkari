# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TarkariItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    unit = scrapy.Field()
    minimum = scrapy.Field()
    maximum = scrapy.Field()
    average = scrapy.Field()
    price = scrapy.Field()
    # datee = scrapy.Field()
    pass
