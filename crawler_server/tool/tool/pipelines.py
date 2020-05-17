from crawler.models import ScrapyItem, Article
import json


class ToolPipeline(object):
    def __init__(self, *args, **kwargs):
        self.articleList = []
    # def from_crawler(cls, crawler):
    #     return cls(
    #         # this will be passed from django view
    #         unique_id=crawler.settings.get('unique_id'),
    #     )
    # @classmethod

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        for article in self.articleList:
            item = Article()
            item.domain = article['domain']
            item.title = article['title']
            item.imageUrl = article['imageUrl']
            item.content = article['content']
            item.topic = article['topic']
            item.save()

    def process_item(self, article, spider):
        print("######## process_item ######, article=", article)
        self.articleList.append(article)

        return article
