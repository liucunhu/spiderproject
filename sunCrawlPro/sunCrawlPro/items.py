# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuncrawlproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=scrapy.Field()
    book_url=scrapy.Field()

class BookChapter(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name=scrapy.Field()
    chapter_name=scrapy.Field()
    chapter_url=scrapy.Field()

class BookConten(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chapter_name = scrapy.Field()
    book_name=scrapy.Field()
    book_content=scrapy.Field()
