# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    author = scrapy.Field()

class JianDanItem(scrapy.Item):
    image_urls = scrapy.Field()

class PengfuItem(scrapy.Item):
    image_urls = scrapy.Field()
