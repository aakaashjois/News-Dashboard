import dispy, random

def parse(url, state, category):

    from bs4 import BeautifulSoup as bs
    import requests
    from ArticleHelper import ArticleHelper
    from pymongo import MongoClient

    soup = bs(requests.get(url).content, 'xml')
    result = []
    for item in soup.channel.find_all('item'):
        helper = ArticleHelper(item.link.string)
        article, length = helper.get_article()
        summary = helper.get_summary(int(length * 0.2))
        date = item.pubDate.string
        post = {
            'article':str(article).encode(encoding='utf-8', errors='ignore'),
            'summary': str(summary).encode(encoding='utf-8', errors='ignore'),
            'category': str(category).encode(encoding='utf-8', errors='ignore'),
            'state': str(state).encode(encoding='utf-8', errors='ignore'),
            'date': str(date).encode(encoding='utf-8', errors='ignore')
        }
        client = MongoClient('172.18.0.1', 8888)
        db = client['articles']
        db.posts.insert_one(post)

if __name__ == '__main__':
    cluster = dispy.JobCluster(parse, depends=['./ArticleHelper.py'])
    jobs = []
    lines = None
    with open('../data.csv', 'r') as f:
        lines = f.readlines()

    for line in lines:
        url, location, category = line.split(',')
        job = cluster.submit(url, location, category)
        jobs.append(job)
        
    for job in jobs:
        job()    
        
    cluster.print_status()
