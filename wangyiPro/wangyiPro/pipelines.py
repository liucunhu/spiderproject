# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class WangyiproPipeline:

    def process_item(self, item, spider):
        filedir='news'
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        filename=os.path.join(filedir,item['title']+'.txt')
        content=item['content']
        with open(filename,'w',encoding='utf-8') as fp:
            fp.write(content)
        return item


