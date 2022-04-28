import scrapy
from huyaall.items import HuyaallItem
import json
class HuyaSpider(scrapy.Spider):
    name = 'huya'
    totalpage=5
    page=1
    #allowed_domains = ['www.huya.com']
    start_urls = ['https://www.huya.com/g/1663']
    # nickname = scrapy.Field()
    # title = scrapy.Field()
    # hot = scrapy.Field()
    def parse(self, response):
        '''
        <div class="list-page" id="js-list-page" data-pages="10">
        :param response:
        :return:
        '''
        # data=response.xpath('//*[@id="js-live-list"]/li')
        totalpage=int(response.xpath('//*[@id="js-list-page"]/@data-pages').extract()[0])
        print('总页面为：',totalpage)
        # for li_tag in data:
        #     item=HuyaallItem()
        #     title=li_tag.xpath('./a[2]/text()').extract()[0]
        #     nickname = li_tag.xpath('./span/span[1]/i/text()').extract()[0]
        #     hot = li_tag.xpath('./span/span[2]/i[2]/text()').extract()[0]
        #     item['title']=title
        #     item['nickname']=nickname
        #     item['hot']=hot


        #print(new_url)
        while 1:
            print(self.page)
            new_url = f'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&callback=getLiveListJsonpCallback&page={self.page}'

            yield scrapy.Request(url=new_url,callback=self.parse_other)
            if self.page>=totalpage:
                break

            self.page=self.page+1

    def parse_other(self,response):

        content=response.text[len('getLiveListJsonpCallback('):-1]
        dict_data=json.loads(content)
        #print(dict_data)
        self.totalPage=dict_data['data']['totalPage']
        totalCount=dict_data['data']['totalCount']
        curpage=dict_data['data']['page']
        print(f'当前页数为：{curpage} 总页数为{self.totalPage} 总数据量{totalCount}')
        for data in dict_data['data']['datas']:
            item = HuyaallItem()
            item['nickname'] = data['nick']
            item['hot']=data['totalCount']
            item['title']=data['roomName']
            yield item
