import scrapy


class MiddlesSpider(scrapy.Spider):
    name = 'middles'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
