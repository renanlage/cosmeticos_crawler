# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductPageItem(scrapy.Item):
    # Define the fields for the product page item
    title = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()

