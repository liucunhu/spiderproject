import scrapy
from imagesPro.items import ImagesproItem

class ZhanzfileSpider(scrapy.Spider):
    name = 'zhanzfile'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list=response.xpath('//*[@id="container"]/div')
        for div_tag in div_list:
            #//*[@id="container"]/div[1]/p/a[1]
            url='https:'+div_tag.xpath('./p/a[1]/@href').extract()[0]
            title=div_tag.xpath('./p/a[1]/text()').extract()[0]+'.jpg'
            yield scrapy.Request(url=url,meta={'title':title},callback=self.get_image)

    def get_image(self,response):
        #/html/body/div[4]/div[5]/div[1]/div[2]/div/div[3]/a/img
        with open('a.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        filename=response.meta['title']
        item=ImagesproItem()
        item['title']=filename
        #/ html / body / div[2] / div[5] / div[1] / div[2] / div / div[3] / a / img
        content='https:'+response.xpath('/html/body/div[2]/div[5]/div[1]/div[2]/div/div[3]/a/img/@src').extract()[0]
        item['image']=content
        #print(filename,content)
        yield item
