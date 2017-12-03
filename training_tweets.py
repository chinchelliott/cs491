#-----------------------------------------------------------------------
# Elliott Miller
# Programming Assignment 3
# CS 491 with Dr. Aibek Musaev
# Due date: 10/15/2017
#-----------------------------------------------------------------------
from __future__ import division
from numpy import average
from utils import txt2words, w2v_load_model
from time import time
import numpy as np
import gensim
from sklearn import svm
import json
import io
from sklearn.naive_bayes import GaussianNB



class DeepTextAnalyzer(object):
    def __init__(self, word2vec_model):
        """
        Construct a DeepTextAnalyzer using the input Word2Vec model
        :param word2vec_model: a trained Word2Vec model
        """
        self._model = word2vec_model

    def txt2vectors(self,txt, is_html):
        """
        Convert input text into an iterator that returns the corresponding vector representation of each
        word in the text, if it exists in the Word2Vec model
        :param txt: input text
        :param is_html: if True, then extract the text from the input HTML
        :return: iterator of vectors created from the words in the text using the Word2Vec model.
        """
        words = txt2words(txt)
        words = [w for w in words if w in self._model]
        if len(words) != 0:
            for w in words:
                yield self._model[w]


    def txt2avg_vector(self, txt, is_html):
        """
        Calculate the average vector representation of the input text
        :param txt: input text
        :param is_html: is the text is a HTML
        :return the average vector of the vector representations of the words in the text
        """
        vectors = self.txt2vectors(txt,is_html=is_html)
        vectors_sum = next(vectors, None)
        if vectors_sum is None:
            return None
        count =1.0
        for v in vectors:
            count += 1
            vectors_sum = np.add(vectors_sum,v)

        #calculate the average vector and replace +infy and -inf with numeric values
        avg_vector = np.nan_to_num(vectors_sum/count)
        return avg_vector

def load_tweets(fname):
    tweets = []
    for line in open(fname):
        data = json.loads(line)
        tweets.append(data)
    return tweets


def w2v_vector(dta, text):
    """
    Given a text, generate Word2Vec vector and return it
    :param dta: DeepTextAnalyzer object
    :param text: input text
    :param label: input label
    """
    vector = dta.txt2avg_vector(text, is_html=False)
    if vector is None:
        return np.zeros(300)
    return [0.0 if v==None else str(v) for v in vector]

def generate_data(tweets):
    model = w2v_load_model('GoogleNews-vectors-negative300.bin')

    dta = DeepTextAnalyzer(model)

    X = list()
    y = list()

    for tweet in tweets:
        vector = w2v_vector(dta, tweet['tweet'])
        X.append(vector)
        y.append(tweet['label'])

    clf = svm.SVC()
    return clf.fit(X,y)


def predict_data (tweets):
    t0 = time()
    model = w2v_load_model('GoogleNews-vectors-negative300.bin')

    dta = DeepTextAnalyzer(model)

    X = list()

    for tweet in tweets:
        vector = w2v_vector(dta, tweet['tweet'])
        X.append(vector)

    return X


if __name__ == '__main__':

    tweets = load_tweets('training_data.txt')

    ctweets_eval = load_tweets('cali_tweets.txt')
    ptweets_eval = load_tweets('port_tweets.txt')

    myclf = generate_data(tweets)

    T_c = list()
    T_c = predict_data(ctweets_eval)

    T_p = list()
    T_p = predict_data(ptweets_eval)

    c_results = []
    p_results = []

    c_results = myclf.predict(T_c)
    p_results = myclf.predict(T_p)

    c_relevant_tweets = 0
    p_relevant_tweets = 0

    for result in c_results:
        if result == '1':
            c_relevant_tweets +=1

    for result in p_results:
        if result == '1':
            p_relevant_tweets +=1


    f = io.open('location_comparison.txt', 'w', encoding = "utf-8")
    f.write(u"Number of Relevant California Wildfire Tweets: <%s>\n" % (c_relevant_tweets))
    f.write(u"Number of Relevant Portugal Wildfire Tweets: <%s>\n" % (p_relevant_tweets))
