# -*- coding: utf-8 -*-
import scrapy


class CosmeticosSpider(scrapy.Spider):
    name = "cosmeticos"
    allowed_domains = ["http://www.epocacosmeticos.com.br"]
    start_urls = (
        'http://www.http://www.epocacosmeticos.com.br/',
    )

    def parse(self, response):
        pass
