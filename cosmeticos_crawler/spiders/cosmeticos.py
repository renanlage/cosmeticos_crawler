# -*- coding: utf-8 -*-
from cosmeticos_crawler.items import ProductPageItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CosmeticosSpider(CrawlSpider):
    name = 'cosmeticos'
    allowed_domains = ['epocacosmeticos.com.br']
    start_urls = [
        'http://www.epocacosmeticos.com.br/'
    ]

    rules = (
        # Extract links matching product pages by the end of url
        # and call method to parse item info
        Rule(LinkExtractor(allow=('./p$',), unique=False), callback='parse_item', follow=True),

        # Only allow department pages to be visited and a few other special pages like offers and outlets
        # Avoid visiting brand pages and visiting redundant pages
        Rule(LinkExtractor(allow=('http://www.epocacosmeticos.com.br/perfumes.',
                                  'http://www.epocacosmeticos.com.br/maquiagem.',
                                  'http://www.epocacosmeticos.com.br/cabelos.',
                                  'http://www.epocacosmeticos.com.br/dermocosmeticos.',
                                  'http://www.epocacosmeticos.com.br/tratamentos.',
                                  'http://www.epocacosmeticos.com.br/corpo-e-banho.',
                                  'outlet', 'oferta', 'blackfriday', 'busca', 'brinde',),

                           # Avoid visiting user account and user services related pages
                           # Avoid discriminating products by price (redundant with other filters) and narrowing the
                           # products views with specificationFilters
                           deny=('account', 'centralatendimento', 'giftList', '/site/', '/checkout', '/cart',
                                 'specificationFilter', 'priceFrom', '/.+http://www.epocacosmeticos.com.br/', './p$',
                                 )), follow=True)
    )

    def parse_item(self, response):
        # and call method to extract data from it
        item = ProductPageItem()
        item['title'] = response.xpath('//head/title/text()').extract()
        item['name'] = response.xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' fn productName ')]/text()").extract()
        item['url'] = response.url
        yield item
