from bs4 import BeautifulSoup as bs
import requests
from ArticleHelper import ArticleHelper
from pymongo import MongoClient


def parse(url, state = '', category = ''):
    soup = bs(requests.get(url).content, 'xml')
    result = []
    for item in soup.channel.find_all('item'):
        helper = ArticleHelper(item.link.string)
        article = helper.get_article()
        print(article)
        summary = helper.get_summary(10)
        print(summary)
        # Extract date
        post = {
            'article':str(article),
            'summary': str(summary),
            'category': str(category),
            'state': str(state)
        }
        client = MongoClient('localhost', 8888)
        db = client['article_database2']
        table = db['article_table']
        posts=db.posts
        post_id = posts.insert_one(post).inserted_id
        print(post_id)

parse('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
