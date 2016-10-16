import scrapy, re
from scrapy_80s_all_movie.items import Scrapy80SAllMovieItem

class Movies_Spider(scrapy.spiders.Spider):
    name = 'movies'
    allowed_domains = ["80s.tw"]
    start_urls = ["http://www.80s.tw/movie/list/----h"]


    def parse(self, reponse):
        item = Scrapy80SAllMovieItem()
        selector = scrapy.Selector(reponse)
        movies = selector.xpath('//div[@class="clearfix noborder block1"]/ul[@class="me1 clearfix"]/li')
	titlePage = selector.xpath('//div[@class="pager"]/a')[-1].xpath("@href").extract()[0]
	mode = re.compile(r'\d+')
	titleNum = mode.findall(titlePage)[0]
        for i in movies:
            name = i.xpath('h3/a/text()').extract()[0]
            link = 'www.80s.tw' + i.xpath('a//@href').extract()[0]
            desc = i.xpath('span[@class="tip"]/text()').extract()[0]
            name = name.replace(' ','').replace('\n','')
            desc = desc.replace(' ','').replace('\n','')
            item['name'] = name
            item['link'] = link
            item['desc'] = desc
            yield item
            nextPage = []
            for j in range(2, int(titleNum)):
                base_url = "http://www.80s.tw/movie/list/----h-p" + str(j)
                nextPage.append(base_url)
            for next_url in nextPage:
                yield scrapy.http.Request(next_url, callback=self.parse)

