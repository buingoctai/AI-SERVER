from scrapy import Spider, Request
from scrapy.selector import Selector
from tool.items import Article
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import HtmlResponse


class IcrawlerSpider(Spider):
    name = 'icrawler'

    allowed_domains = ["tuoitre.vn"]
    start_urls = [
        'https://congnghe.tuoitre.vn/'
    ]

    def parse(self, response):
        if response.url == 'https://congnghe.tuoitre.vn/':
            lastedArticlesList = response.css(
                'ul.list-news-content li a::attr(href)').getall()
            print('########## lastedArticlesList=', lastedArticlesList)
            lastedArticlesList = list(dict.fromkeys(lastedArticlesList))
            print('##################### lastedArticlesList=', lastedArticlesList)
            for link in lastedArticlesList:
                print("################## link=", link)

                request = Request('https://tuoitre.vn/'+link,
                                  callback=self.parse)
                yield request
        else:
            # print('########## response.url=', response.url)
            title = response.css('h1.article-title::text').get()
            imageUrl = response.css(
                'div.main-content-body img::attr(src)').get()
            if imageUrl is None:
                imageUrl = "https://afmec.org/images/no-image-available-icon.jpg"
            content = ''
            intro = response.xpath(
                '//*[@id="mainContentDetail"]/div/div[2]/h2/text()').get()
            content = content+intro
            contentList = Selector(response).xpath(
                '//*[@id="main-detail-body"]/p')
            for subContent in contentList:
                sub = subContent.xpath('text()').get()
                if sub is None:
                    continue
                else:
                    content = content+sub
            article = Article()
            article['domain'] = self.allowed_domains[0]
            article['title'] = title
            article['content'] = content
            article['topic'] = self.start_urls[0]
            article['imageUrl'] = imageUrl
            yield article
