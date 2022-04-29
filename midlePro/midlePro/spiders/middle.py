import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.ip111.cn/']

    def parse(self, response):
        page_text=response.text
        #print(page_text)
        with open('ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
