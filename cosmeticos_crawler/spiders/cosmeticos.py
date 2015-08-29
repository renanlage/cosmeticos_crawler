# -*- coding: utf-8 -*-
import scrapy

from cosmeticos_crawler.items import ProductPageItem


class CosmeticosSpider(scrapy.Spider):
    name = 'cosmeticos'
    allowed_domains = ['epocacosmeticos.com.br']
    start_urls = [
        'http://www.epocacosmeticos.com.br/'
    ]

    def parse(self, response):
        # Identify a product page by end of url
        # and call method to extract data from it
        if response.url.endswith('/p'):
            self.parse_item(response)

        # If it's not a product page call parse for all other links
        for href in response.xpath('//a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse)

    def parse_item(self, response):
            # Set item attributes with data extracted from the page
            item = ProductPageItem()
            item['title'] = response.xpath('//head/title/text()').extract()
            item['name'] = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' fn productName ')]/text()").extract()
            item['url'] = response.url
            yield item
