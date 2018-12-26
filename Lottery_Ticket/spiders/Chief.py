# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy_redis.spiders import RedisSpider
from Lottery_Ticket.items import LotteryTicketItem
from redis import Redis


# lpush Chirf:Start 'http://kaijiang.500.com/shtml/ssq/18149.shtml'

class ChiefSpider(scrapy.Spider):
# redis 可能的分布式
# class ChiefSpider(RedisSpider):
    name = 'Chief'
    # redis_key = 'Chief:Start'

    # __init__方法必须按规定写，使用时只需要修改super()里的类名参数即可
    # def __init__(self, *args, **kwargs):
    #     super(ChiefSpider,self).__init__( *args, **kwargs)


    allowed_domains = ['kaijiang.500.com']
    # url = 'http://kaijiang.500.com/shtml/ssq/{}.shtml'
    url = 'http://kaijiang.500.com/shtml/ssq/18149.shtml'
    start_urls = [url]
    # for x in range(18149):
    #     if len(str(x)) != 5:
    #         x = (5 - len(str(x))) * str('0') + str(x)
    #     if int(str(x)[2:]) > 160:
    #         pass
    #     else:
    #         urls = url.format(str(x))
    #         start_urls.append(urls)

    def parse(self, response):

        # red = Redis()

        # red.lpush('Chief:Start',url)

        item = LotteryTicketItem()
        # 网页上一页
        # print(response.text)
        # next_page2 = response.css('td.a::attr("href")')
        # print(next_page2)
        # print('-----------------------------')
        # if response.status != 200:
        #     print('--------%d---------'%response.status)
        #     yield ''
        ball_data = response.css('strong::text')[-1].extract()
        item['ball_data'] = ball_data
        red_ball = response.css('li.ball_red::text')
        blue_ball = response.css('li.ball_blue::text')
        reds = '-'.join([red.extract() for red in red_ball])
        try:
            blues = blue_ball[-1].extract()
        except IndexError:
            item['blue_ball'] = ''
        else:
            item['blue_ball'] = blues
        item['red_ball'] = reds
        ball_sequences = response.css('tr > td::text')
        sales = response.css('span.cfont1::text')
        if len(sales) == 2:
            # 销量
            item['sales_volums'] = sales[0].extract().replace(',','').replace('元','')
            # 奖池金额
            item['All_Bouns'] = sales[1].extract().replace(',','').replace('元','')
        Shares_list = list()
        for ball_sequence in ball_sequences:
            num = len(ball_sequence.extract().strip().split(' '))
            if num == 6:
                try:
                    ball_seq = [x for x in ball_sequence.extract().strip().split(' ') if len(x) == 2]
                except ValueError:
                    pass
            # 奖池提取
            ball_Shares = ball_sequence.extract().replace('\r','').replace('\t','').replace('\n','').replace(' ','')
            if ball_Shares == '':
                pass
            else:
                # if '等奖' in ball_Shares:
                try:
                    Shares_list.append(int(ball_Shares.replace(',','')))
                except ValueError:
                    pass
        if len(Shares_list) < 12:
            pass
        else:
            if Shares_list[-1] == 5:
                item['Sixth_price_Bonus'] = Shares_list[-2]
                item['Fifth_price_Bonus'] = Shares_list[-4]
                item['Fourth_price_Bonus'] = Shares_list[-6]
                item['Third_price_Bonus'] = Shares_list[-8]
                item['Second_price_NumShare'] = Shares_list[-9]
                item['Second_price_Bonus'] = Shares_list[-10]
                item['First_price_NumShare'] = Shares_list[-11]
                item['First_price_Bonus'] = Shares_list[-12]
            else:
                pass
        try:
            item['ball_sequence'] = '>'.join(ball_seq)
        except UnboundLocalError:
            item['ball_sequence'] = ''
        # print(item)
        yield item

        HXS = HtmlXPathSelector(response)
        xx = HXS.select('//td/a[contains(@href,"kaijiang.500.com")]/@href')
        if xx:
            url = xx.extract()[0]
            if 'http' in url:
                newUrl = url
            else:
                newUrl = 'http:' + url
            print(newUrl)
            yield scrapy.Request(newUrl, callback=self.parse)
