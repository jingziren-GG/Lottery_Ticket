# -*- coding: utf-8 -*-
import json
import pymssql
import sys
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LotteryTicketPipeline(object):
    def __init__(self):
        # 存入yyy.json 文件中
        self.filename = open('yyy.json','ab+')

    def process_item(self, item, spider):
        text = json.dumps(dict(item),ensure_ascii=False) + ';\n'
        self.filename.write(text.encode('utf-8'))
        return item


    def close_spider(self,spider):
        self.filename.close()