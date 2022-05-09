import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qb5.tw/quanben/1']
    link=LinkExtractor(allow=r'quanben/\d+')
    link_detail=LinkExtractor(allow=r'book_\d+/')
    link_detail = LinkExtractor(allow=r'book_\d+/')
    #book_798 / 472065.html
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_book_chapter', follow=True),
    )

    def parse_item(self, response):
        item = {}
        book_tag_list=response.xpath('//*[@id="tlist"]/ul/li')
        for book_li in book_tag_list:

            book_name=book_li.xpath('./div[1]/a/text()').extract()[0]
            book_url = book_li.xpath('./div[1]/a/@href').extract()[0]
            book_author=book_li.xpath('./div[3]/text()').extract()[0]
            #print(book_name,book_url,book_author)
            break


        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

    def parse_book_chapter(self,response):
        title=response.xpath('//*[@id="info"]/h1/text()').extract()[0]
        author=response.xpath('//*[@id="info"]/h1/small/a/text()').extract()[0]
        chapter=response.xpath('/html/body/div[4]/dl/dd')

        for content in chapter:
            try:
                content_url=content.xpath('./a/@href').extract()[0]
                content_name=content.xpath('./a/text()').extract()[0]
                #print(f'小说{title}章节名称{content_name}章节地址{content_url}')
            except Exception as e:

                print(e)



