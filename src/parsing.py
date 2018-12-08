def parse(url, state = '', category = ''):
    from bs4 import BeautifulSoup as bs
    import requests
    from ArticleHelper import ArticleHelper
    from pymongo import MongoClient
    soup = bs(requests.get(url).content, 'xml')
    result = []
    for item in soup.channel.find_all('item'):
        helper = ArticleHelper(item.link.string)
        article = helper.get_article()
        summary = helper.get_summary(10)
        # Extract date
        post = {
            'article':str(article),
            'summary': str(summary),
            'category': str(category),
            'state': str(state)
        }
        client = MongoClient('172.18.0.1', 8888)
        db = client['party']
        posts=db.posts
        post_id = posts.insert_one(post).inserted_id
