import scrapy
from selenium.webdriver import Chrome
from wangyiPro.items import WangyiproItem


class WangyinewSpider(scrapy.Spider):
    name = 'wangyinew'
    #allowed_domains = ['www.xxxx.com']
    start_urls = ['https://news.163.com/']
    bro = Chrome(executable_path=r"D:\myfile\bdriver\chromedriver.exe")
    #bro.get('https://www.baidu.com')
    module_url_list = []
    def parse(self, response):
        moudle_ul=response.xpath('//*[@id="index2016_wrap"]/div[2]/div[2]/div[3]/div[2]/div[5]/div/div[1]/ul/li|//*[@id="index2016_wrap"]/div[2]/div[2]/div[3]/div[2]/div[5]/div/div[1]/div/a')
        #moudle_ul2=response.xpath('')

        for url_tag in moudle_ul:
            url=url_tag.xpath('./a/@href|./@href').extract()[0]
            if 'https' in url:
                self.module_url_list.append(url)
                yield scrapy.Request(url=url,callback=self.get_item_url)


        #print(self.module_url_list)
    def get_item_url(self,response):

        detail_div=response.xpath('/html/body/div/div[3]/div[5]/div[3]/div/ul/li[1]/div/div')

        for div_tag in detail_div:

            #//*[@id="test_temple"]/./div/div[1]/h3/a
            try:
                detail_url=div_tag.xpath('./a/@href').extract()[0]
                detail_title=div_tag.xpath('./div/div[1]/h3/a/text()').extract()[0]
                yield scrapy.Request(url=detail_url,meta={'title':detail_title},callback=self.get_content)
                #print('获取数据为：================\nurl-', detail_url, '\n ', detail_title, '==========\n')
            except Exception as e:
                print(e)
                print(div_tag.xpath('./a/@href').extract())
    def get_content(self,reponse):

        title=reponse.meta['title']
        content='\n'.join(reponse.xpath('//*[@id="content"]//p//text()').extract())
        item=WangyiproItem()
        item['title']=title
        item['content']=content
        yield item
    def close(self):
        self.bro.close()







