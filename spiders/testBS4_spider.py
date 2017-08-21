import scrapy
from bs4 import BeautifulSoup
import requests
import re

#定義要爬的資料
class NobelItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    category = scrapy.Field()
    link = scrapy.Field()
    country = scrapy.Field()



#建立蜘蛛
class NWinnerSpider(scrapy.Spider):
    name = 'testBS4_spider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ["https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country"]

    def parse(self, response):
        wdata = {}
        Soup = BeautifulSoup(response.body)

        host = 'https://en.wikipedia.org/'

        # 找每個<h2>
        h2s = Soup.find_all('h2')
        for h2 in h2s:

            if h2.find('span', {'class': 'mw-headline'}):
                country = h2.find('span', {'class': 'mw-headline'}).text

                if country != 'Summary' and country != 'See also' and country != 'References':

                    lis = h2.find_next("ol").find_all('li')
                    for li in lis:
                        name = li.text.split(',')[0].strip()
                        if li.find('a').text != 'Leopold Ružička':
                            category = li.text.split(',')[-2].strip()
                            year = re.findall('\d{4}', li.text)
                        else:
                            category = ''
                            year = ''
                        link = li

                        if category:
                           pass
                        else:
                            category = ''

                        if year:
                            pass
                        else:
                            year = '0'



                        link = host + li.find('a')['href']

                        wdata['name']= name
                        wdata['category'] = category
                        wdata['year'] = year
                        wdata['link'] = link
                        wdata['country'] = country

                        items = NobelItem(**wdata)

                        yield items


