from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.utils import get_stop_words
import pickle
import os
from os.path import isfile, isdir

LANGUAGE = 'english'
FILE_NAME = 'test'

def summarize(url, num_sentences=3):
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    summarizer = ReductionSummarizer(Stemmer(LANGUAGE))
    summarizer.stop_words = get_stop_words(LANGUAGE)
    summary = [str(sentence) for sentence in summarizer(parser.document, num_sentences)]
    return ''.join(summary)
