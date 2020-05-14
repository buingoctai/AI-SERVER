from crawler.models import ScrapyItem
import json


class ToolPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        self.items = []

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            # this will be passed from django view
            unique_id=crawler.settings.get('unique_id'),
        )

    def close_spider(self, spider):
        # And here we are saving our crawled data with django models.
        print("--------close_spider------------")
        item = ScrapyItem()
        item.unique_id = self.unique_id
        item.data = json.dumps(self.items)
        item.save()

    def process_item(self, item, spider):
        print("--------process_item------------, item=", item)
        print("--------process_item------------, spider=", spider)

        self.items.append(item['text'])
        # self.items.append(item['Comment'])

        return item
