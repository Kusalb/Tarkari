# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    amount = scrapy.Field()
    info = scrapy.Field()
    product = scrapy.Field()
    weight = scrapy.Field()
    currency = scrapy.Field()
    price = scrapy.Field()
    datee = scrapy.Field()
    pass
