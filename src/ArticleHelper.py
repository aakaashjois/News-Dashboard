from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


class ArticleHelper:
    def __init__(self):
        language = 'english'
        self.tokenizer = Tokenizer(language)
        self.summarizer = Summarizer(Stemmer(language))
        self.summarizer.stop_words = get_stop_words(language)


    def get_article(self, url):
        article = HtmlParser.from_url(url, self.tokenizer)
        return article.document

    def get_summary(self, article, num_sentences):
        summary = [str(sentence) for sentence in self.summarizer(article, num_sentences)]
        return ''.join(summary)
