import scrapy


class MiddledemoSpider(scrapy.Spider):
    name = 'middledemo'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
