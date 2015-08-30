# -*- coding: utf-8 -*-
from cosmeticos_crawler.items import ProductPageItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CosmeticosSlowSpider(CrawlSpider):
    name = 'cosmeticos'
    allowed_domains = ['epocacosmeticos.com.br']
    start_urls = [
        'http://www.epocacosmeticos.com.br/'
    ]

    rules = (
        # Extract links matching product pages by the end of url
        # and call method to parse item info
        Rule(LinkExtractor(allow=('./p$', ), unique=False), callback='parse_item', follow=True),

        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(deny=('account', 'centralatendimento', 'giftList', '/site/', '/checkout', '/cart',
                                 'specificationFilter', 'priceFrom', '/.+http://www.epocacosmeticos.com.br/', './p$',
                                )), follow=True),
    )

    def parse_item(self, response):
        # and call method to extract data from it
        item = ProductPageItem()
        item['title'] = response.xpath('//head/title/text()').extract()
        item['name'] = response.xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' fn productName ')]/text()").extract()
        item['url'] = response.url
        yield item
