from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


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
        summary = [str(sentence) for sentence in self.summarizer(self.article.document, num_sentences)]
        return ''.join(summary)
