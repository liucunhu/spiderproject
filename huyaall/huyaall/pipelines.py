# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class HuyaallPipeline:
    fp=None
    filedir='spiderdata/'
    def open_spider(self,spider):
        print('开始下载数据')
        if not os.path.exists(self.filedir):
            os.mkdir(self.filedir)

        self.fp=open(self.filedir+'huya.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        result=f"{item['title']}||{item['nickname']}||{item['hot']}\n"
        self.fp.write(result)
        #print(item['title'],':保存成功')
        return item

    def close_spider(self,spider):
        self.fp.close()
        print('数据获取完成')