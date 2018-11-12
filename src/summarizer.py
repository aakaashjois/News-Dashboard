from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.reduction import ReductionSummarizer
from sumy.utils import get_stop_words

LANGUAGE = 'english'
FILE_NAME = 'test'

parser = PlaintextParser.from_file('data/{}.txt'.format(FILE_NAME), Tokenizer(LANGUAGE))
summarizer = ReductionSummarizer(Stemmer(LANGUAGE))
summarizer.stop_words = get_stop_words(LANGUAGE)

summary = [str(sentence) for sentence in summarizer(parser.document, 3)]
with open('out/{}_summary.txt'.format(FILE_NAME), 'w') as out:
    out.write(' '.join(summary))