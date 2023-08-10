import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from datetime import datetime

df = pd.read_csv('data/movies_clean.csv')
# df.sample(5)
# df.info()


def clean_text(text):
    '''Make text lowercase,remove punctuation
    .'''
    text = str(text).lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    return text

q = df['title'] + " " + df['overview']
q  = q.apply(lambda x:clean_text(x))


#create the TF-IDF model
MAX_DF     = 0.95
MIN_DF     = 2
tfidf = TfidfVectorizer(#max_df=MAX_DF, min_df=MIN_DF, \
                        #max_features=10000,\
                        stop_words='english', token_pattern = r"\b\w{3,}\b")

content = q.dropna()[:20000]
tfidf_matrix = tfidf.fit_transform(content)

#tfidf_matrix.shape()


t = datetime.now()
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
#print (type (cosine_similarities))
cosine_similarity_scores = list(enumerate(cosine_similarities[0]))
cosine_similarity_scores = sorted(cosine_similarity_scores, key=lambda x: x[1], reverse=True)
print (cosine_similarity_scores[:5])

for i in cosine_similarity_scores[:6]:
    print (df.loc[i[0]].title, i[1])



print ('Tiempo : ', round((datetime.now()-t).total_seconds(), 2) )
print (len(df.loc[123].overview))