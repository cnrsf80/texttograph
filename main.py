from sklearn.feature_extraction.text import CountVectorizer

def build_adjacency_matrix(corpus):
    vectorizer = CountVectorizer()
    print(vectorizer.fit_transform(corpus).todense())





corpus = [
'All my cats in a row',
'When my cat sits down, she looks like a Furby toy!',
'The cat from outer space',
'Sunshine loves to sit like this for some reason.'
]


