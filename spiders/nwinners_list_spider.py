import scrapy
import re

#定義要爬的資料
class NWinnerItem(scrapy.Item):
    country = scrapy.Field()
    name = scrapy.Field()
    year = scrapy.Field()
    category = scrapy.Field()
    born_in = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()

#建立蜘蛛
class NWinnerSpider(scrapy.Spider):
    name = 'nwinners_list'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country"]

    def parse(self, response):

        h2s = response.xpath('//h2')
        for h2 in h2s:
            country = h2.xpath('span[@class="mw-headline"]/text()').extract()

            if country:
                winners = h2.xpath('following-sibling::ol[1]')

                for w in winners.xpath('li'):
                    text = w.xpath('descendant-or-self::text()').extract()
                    wdata = process_winner_li(w,country[0])
                    items = NWinnerItem(**wdata)

                    yield items




BASE_URL = 'http://en.wikipedia.org'

# 解析出生國家、年代
def process_winner_li(w,country=None):

    wdata={}
    wdata['link'] = BASE_URL+ w.xpath('a/@href').extract()[0]

    text = ' '.join(w.xpath('descendant-or-self::text()').extract())

    wdata['name'] = text.split(',')[0].strip()

    year = re.findall('\d{4}',text)
    if year:
        wdata['year'] = int(year[0])
    else:
        wdata['year'] = 0
        print('no year in ', text)

    category = re.findall('Physics | Chemistry | Physiology or Medicine | Literature | Peace | Economics', text)

    if category:
        wdata['category'] = category[0]
    else:
        wdata['category'] = ''
        print('no category in ', text)

    if country:
        if text.find('*') != -1:
            wdata['country'] = ''
            wdata['born_in'] = country
        else:
            wdata['country'] = country
            wdata['born_in'] = ''

    wdata['text'] =text
    return wdata


