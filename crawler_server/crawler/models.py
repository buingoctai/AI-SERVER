import json
from django.db import models
from django.utils import timezone


class ScrapyItem(models.Model):
    unique_id = models.CharField(max_length=100, null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {
            'data': json.loads(self.data),
            'date': self.date
        }
        return data

    def __str__(self):
        return self.unique_id


class Article(models.Model):
    domain = models.CharField(max_length=50, null=False)
    title = models.TextField()
    content = models.TextField()
    topic = models.CharField(max_length=100, null=True)
    crawlDate = models.DateTimeField(default=timezone.now)
    imageUrl = models.TextField()

    @property
    def to_dict(self):
        data = {
            'domain': self.domain,
            'title': self.title,
            'content': self.content,
            'topic': self.topic,
            'crawlDate': self.crawlDate,
            'imageUrl': self.imageUrl
        }
        return data

    def __str__(self):
        return self.crawlDate
