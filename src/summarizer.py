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

if(isfile('filenumobj.pkl')):
    with open('filenumobj.pkl', 'rb') as picklefile:
        num = pickle.load(picklefile)
else:
    num = 1

if(not isdir('out')):
    os.makedirs('out')

parser = HtmlParser.from_url('https://www.theguardian.com/us-news/2018/nov/17/reublicans-look-to-new-hampshire-for-a-potential-trump-2020-challenger', Tokenizer(LANGUAGE))
summarizer = ReductionSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)

summary = [str(sentence) for sentence in summarizer(parser.document, 3)]
with open('out/{}{}_summary.txt'.format(FILE_NAME, num), 'w') as out:
    out.write(' '.join(summary))
num+=1
with open('filenumobj.pkl', 'wb') as picklefile:
    pickle.dump(num, picklefile)
