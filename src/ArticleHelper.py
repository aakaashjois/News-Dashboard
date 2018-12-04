from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer


class ArticleHelper:
    def __init__(self):
        language = 'english'
        self.tokenizer = Tokenizer(self.language)
        self.summarizer = Summarizer(Stemmer(self.language))
        self.summarizer.stop_words = get_stop_words(self.language)


    def get_article(self, url):
        article = HtmlParser.from_url(url, Tokenizer)
        return article.document

    def get_summary(self, article, num_sentences):
        summary = [str(sentence) for sentence in self.summarizer(article, num_sentences)]
        return ''.join(summary)
