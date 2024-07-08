import scrapy
from scrapy.crawler import CrawlerProcess

class YT_view(scrapy.Spider):
    name = 'views'
    start_urls = ['https://free-proxy-list.net']

    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding' : 'gzip, deflate, br, zstd',
        'Accept-Language' : 'en-US,en;q=0.9',
        'Cache-Control' : 'max-age=0',
        'Sec-Fetch-Mode' : 'navigate',
        'Sec-Fetch-Site' : 'none',
        'Sec-Fetch-User' : '?1',
        'Upgrade-Insecure-Requests' : '1',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }

    def parse(self, response):
        #print(response.text)

        table = response.css('table')
        rows = table.css('tr')

        #print(rows.getall())

        cols = [row.css('td::text').getall() for row in rows]
        #print(cols)

        proxies = []

        for col in cols:
           if col and col[4] == 'elite proxy' and col[6] == 'yes':
               proxies.append('https://' + col[0] + ':' + col[1])






#run spider
process = CrawlerProcess()
process.crawl(YT_view)
process.start()