# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider
from cosmeticos_crawler.items import ProductPageItem


class CosmeticosSitemapSpider(SitemapSpider):
    name = "cosmeticos_sitemap"
    sitemap_urls = [
        'http://www.epocacosmeticos.com.br/sitemap-produtos-1.xml',
        'http://www.epocacosmeticos.com.br/sitemap-produtos-2.xml'
    ]

    def parse(self, response):
        # Set item attributes with data extracted from the page
        item = ProductPageItem()
        item['title'] = response.xpath('//head/title/text()').extract()
        item['name'] = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' fn productName ')]/text()").extract()
        item['url'] = response.url
        yield item
