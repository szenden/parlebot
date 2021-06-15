import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.stem import SnowballStemmer
from nltk.stem.snowball import DutchStemmer
from gensim.matutils import cossim, sparse2full
import numpy as np
from operator import itemgetter

def rank_similarities(doc_set, question_vect, method='hellinger'):
    """
    Computes similarities between documents. Returns list of lists, sorted by
    similarity score.

    Keyword arguments:
    doc_vect --
    question_vect --
    method -- 
    """

    if method == 'hellinger':
        # print(question_vect)
        for article in doc_set:
            sim = np.sqrt(0.5 * ((np.sqrt(question_vect) - np.sqrt(article['vector']))**2).sum())
            article['similarity'] = sim

        # print the titles of the most relevant documents
        article_ranking = sorted(doc_set, key=itemgetter('similarity'))
        for index, article in enumerate(article_ranking):
            print('{}: Similarity:{}. Title:{}'.format(index, article['similarity'], article['title']))
        return doc_set
    else:
        pass


def doc_vect(doc_set, questions):
    """
    Transforms documents and questions to vectors to be used for similarity
    ranking. 
    Returns list of ([document vector list], questions vector).

    Keyword arguments:
    doc_set -- Dict object of retrieved documents found py articles.py
    questions -- List object of questions from the question set
    """

    # specify the number of topics we want to find from the documents
    n_topics = 10
    n_top_words = 10

    # load dutch stop words list and parse to list
    infile = open('code/stopwords-nl.txt', 'r')
    stop_words = [line.strip() for line in infile.readlines()]

    # instantiate vectorizer and fit on the entire corpus
    tfidf_vectorizer = TfidfVectorizer(stop_words=stop_words, ngram_range=(1,2))

    corpus = build_corpus(doc_set, questions)
    tfidf = tfidf_vectorizer.fit_transform(corpus)

    # instantiate lda model
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=5,
                                    learning_method='online',
                                    learning_offset=50.,
                                    random_state=0)
    lda.fit(tfidf)

    # transform combined questions to vector
    question_str = ''.join(questions)
    question_vector = tfidf_vectorizer.transform([question_str])
    question_vector = lda.transform(question_vector)
    
    # transform all article text to vectors
    for article in doc_set:
        article_vector_temp = tfidf_vectorizer.transform([article['text']])
        article['vector'] = lda.transform(article_vector_temp)

    tf_feature_names = tfidf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words)

    return [doc_set, question_vector]
    

def build_corpus(doc_set, questions):
    """
    Build corpus of all words in the retrieved documents and the question set.
    Returns list of documents that can be used to fit the CountVectorizer.

    Keyword arguments:
    doc_set -- Dict object of retrieved documents found py articles.py
    questions -- List object of questions from the question set
    """

    # combine all text from the documents
    doc_text = []
    for article in doc_set:
        doc_text.append(article['text'])

    # combine all text from the questions
    question_index = 2
    question_text = ''
    for row in questions:
        question_text += row[question_index]

    # add the text from the questions to the document corpus
    doc_text.append(question_text)

    return doc_text
    

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()