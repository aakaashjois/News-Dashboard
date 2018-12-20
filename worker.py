import dispy


def parse(url, state, category):
    """
    This method contains all the necessary imports, classes and methods to ship to the worker nodes.
    
    Arguments:
        url {string} -- URL on which the parser is run.
        state {string} -- The "State" of the URL. Can be None.
        category {string} -- The "Category" of the URL. Can be None.
    
    Returns:
        None -- Does not return anything,
    """

    import requests
    from bs4 import BeautifulSoup as bs
    from pymongo import MongoClient
    from sumy.parsers.html import HtmlParser
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.summarizers.lsa import LsaSummarizer as Summarizer
    from sumy.nlp.stemmers import Stemmer
    from sumy.utils import get_stop_words

    HOST = '172.18.0.1' # The host URL at which MongoDB is running
    PORT = 8888 # The port at which MongoDB is running

    class ArticleHelper:
        def __init__(self, url):
            language = 'english'
            self.tokenizer = Tokenizer(language)
            self.summarizer = Summarizer(Stemmer(language))
            self.summarizer.stop_words = get_stop_words(language)
            self.article = HtmlParser.from_url(url, self.tokenizer)
            

        def get_article(self):
            sentences = [*self.article.document.sentences]
            texts = [sentence._text for sentence in sentences]
            return ' '.join(texts), len(sentences)


        def get_summary(self, num_sentences):
            return ''.join([str(sentence) for sentence in self.summarizer(self.article.document, num_sentences)])

    soup = bs(requests.get(url).content, 'xml')
    for item in soup.channel.find_all('item'):
        helper = ArticleHelper(item.link.string)
        article, length = helper.get_article()
        summary = helper.get_summary(int(length * 0.2))
        date = item.pubDate.string
        post = {
            'article':str(article),
            'summary': str(summary),
            'category': str(category),
            'state': str(state),
            'date': str(date)
        }
        client = MongoClient(HOST, PORT)
        db = client['articles']
        try:
            db.posts.insert_one(post)
        except Exception as e:
            continue


if __name__ == '__main__':
    cluster = dispy.JobCluster(parse)
    jobs = []
    with open('data.csv', 'r') as f:
        lines = f.readlines()

    for line in lines:
        url, location, category = line.split(',')
        job = cluster.submit(url, location, category)
        jobs.append(job)
        
    for job in jobs:
        job()    
        
    cluster.print_status()
