"""
author --> Adwaith Rajesh
find me on ig @__adwaith__rajesh_
"""

try:
    from api_key import Keys

except ImportError:
    from .api_key import Keys

finally:
    from newsapi import NewsApiClient
    import datetime


class News(Keys):

    def __init__(self):
        self.news_api = NewsApiClient(api_key=self.new_api_key)
        self.news_list = {}

    def fetch_news(self, category):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)

        self.news_list.clear()

        query = category
        top_headlines = self.news_api.get_everything\
            (q=query, language='en', sort_by='relevancy', page=1, domains='bbc.co.uk,techcrunch.com, .in',
             sources='bbc-news,the-verge, the-hindu, the-times-of-india', from_param=yesterday, to=today)

        articles = top_headlines['articles']

        counter = 0
        for article in articles:
            news_tuple = (article['title'], article['description'], article['content'], article['url'])
            self.news_list[counter] = news_tuple
            counter += 1
