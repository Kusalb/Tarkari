# -*- coding: utf-8 -*-
import scrapy
from ..items import TarkariItem

class TarkariSpider(scrapy.Spider):
    name = 'tarkari'
    start_urls = ['https://www.ktm2day.com/vegetables-price-in-nepali-market/']

    def parse(self, response):
        items = TarkariItem()
        name = response.css('.row0 td:nth-child(1) , .row1 td:nth-child(1)').css('::text').extract()
        unit = response.css('.row0 td:nth-child(2) , .row1 td:nth-child(2)').css('::text').extract()
        minimum = response.css('.row0 td:nth-child(3) , .row1 td:nth-child(3)').css('::text').extract()
        maximum = response.css('.row0 td:nth-child(4) , .row1 td:nth-child(4)').css('::text').extract()
        average = response.css('.row0 td:nth-child(5) , .row1 td:nth-child(5)').css('::text').extract()
        date = response.css('h4 span').css('::text').extract()
        sk = date[0]
        br = sk.split(' ')
        print(br)
        datee = br[6] + br[5] + ',' + br[7]


        items['name'] = name
        items['unit'] = unit
        items['minimum'] = minimum
        items['maximum'] = maximum
        items['average'] = average
        items['datee'] = datee
        yield items


