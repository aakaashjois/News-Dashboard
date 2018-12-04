from bs4 import BeautifulSoup as bs
import requests
import ArticleHelper
from pymongo import MongoClient


def parse(url, state = '', category = ''):
    soup = bs(requests.get(url).content, 'xml')
    result = []
    for item in soup.channel.find_all('item'):
        helper = ArticleHelper()
        article = helper.get_article(item.link.string)
        summary = helper.get_summary(article, 10)
        # Extract date
        post = {
            'article': article,
            'summary': summary,
            'category': category,
            'state': state
        }
        client = MongoClient('localhost', '8888')
        db = client['article_database']
        table = db['article_table']
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        print(post_id)
