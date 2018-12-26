# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class LotteryTicketItem(scrapy.Item):
    # define the fields for your item here like:
    red_ball = scrapy.Field()
    blue_ball = scrapy.Field()
    ball_sequence = scrapy.Field()
    ball_data = scrapy.Field()
    # 总销量
    sales_volums = scrapy.Field()
    # 总奖金
    All_Bouns = scrapy.Field()
    # 各奖项的中奖注数和中奖金额
    First_price_NumShare = scrapy.Field()
    First_price_Bonus = scrapy.Field()
    Second_price_NumShare = scrapy.Field()
    Second_price_Bonus = scrapy.Field()
    Third_price_Bonus = scrapy.Field() # 3000
    Fourth_price_Bonus = scrapy.Field() # 200
    Fifth_price_Bonus = scrapy.Field() # 10
    Sixth_price_Bonus = scrapy.Field() # 5


class LotteryLucky(ItemLoader):
    Lottery = LotteryTicketItem
    # Lottery_url



