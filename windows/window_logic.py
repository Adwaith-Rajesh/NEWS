import os
import sys

sys.path.insert(1, os.path.split(os.getcwd())[0])

from news_api.news import News
from news_api.weather import Weather


class Display:

    def __init__(self):
        self.topics = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
        self.news = News()
        self.weather_ = Weather()

    def show_info(self, num):
        category = self.topics[num]
        self.news.fetch_news(category)

        return self.news.news_list

    def weather(self):
        return self.weather_.get_info()
