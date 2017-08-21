# wiki_Scrapy_test
for practice using Scrapy to get data from wikipedia

###說明###

spider 放在spider裡面，都是在爬(https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_country)
這個頁面的所有的得獎者。

nwinners_list_spider.py  --> 這個是使用xpath。
testBS4_spider.py        --> 是使用BeautifulSoup來寫。

###啟用辦法###

Spider的名字寫在每個spider的.py檔，裡面的name。

cmd在nobel_winner目錄  => scrapy nwinner_list -o (自己命名).json     (執行nwinner_list_spider.py) 
                      => scrapy testBS4_spider -o (自己命名).json    (執行testBS4-Spider.py)

就會產生.json檔在目錄中。
  
