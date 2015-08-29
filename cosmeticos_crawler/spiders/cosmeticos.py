# -*- coding: utf-8 -*-
import scrapy

from cosmeticos_crawler.items import ProductPageItem


class CosmeticosSpider(scrapy.CrawlSpider):
    name = "cosmeticos"
    allowed_domains = ("http://www.epocacosmeticos.com.br")
    start_urls = ('http://www.http://www.epocacosmeticos.com.br/')

    def parse(self, response):
        pass

    def parse_item(self, response):
        # Identify a product page by end of url
        if response.url.endswith('/p')
            item = ProductPageItem()
            item['title'] = response.xpath('//head/title/text()').extract()
            item['name'] = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' fn productName ')]/text()").extract()
            item['url'] = response.url
            yield item
