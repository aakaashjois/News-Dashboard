from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_features=5)
corpus = [
    'ICC Women’s World T20: Mandhana powers India to 167-8 against Australia',
    'World ATP Finals: Zverev shocks Federer',
    'World Boxing championship: Pinki shows her mettle against Anush',
    'Prajnesh outplays, out-thinks Myneni',
    'Hamish scores unbeaten century',
    'ICC Women’s World T20: England, Windies make semifinals',
    'Big moment for debutants',
    'Defourny tops the points table',
    'Karthik sets the track ablaze',
    'World Chess Championship: Even at half-way',
    'Vinales takes first pole of season',
    'Kostic corners glory'
]

X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())