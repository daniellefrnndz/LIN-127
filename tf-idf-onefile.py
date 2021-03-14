import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

"""
import glob
album_filenames = glob.glob('C:\\Users\\Eric\\Desktop\\data\\comm_success\\*.txt') 

lyrics_as_list_of_strings = []

for album in album_filenames:
    album_open = open(album, 'r', errors='ignore')  
    album_read = album_open.read()
    lyrics_as_list_of_strings.append(album_read)
"""

#'/home/dfer/project/commercially_successful_group_all_lyrics.txt'
lyrics_file = 'C:\\Users\\Eric\\Desktop\\data\\commercially_successful_group_all_lyrics.txt'
lyrics_file_open = open(lyrics_file, 'r', errors='ignore')       
corpus = lyrics_file_open.read()
corpus = corpus.split('###############################################')

vectorizer = TfidfVectorizer(input='content',
                             strip_accents='ascii', 
                             analyzer='word', 
                             stop_words='english', 
                             use_idf=True, 
                             smooth_idf=True,
                             sublinear_tf=True, 
                             ngram_range=(1,1)
                             )

tfidf_vectors = vectorizer.fit_transform(corpus)

tfidf_output = tfidf_vectors[0]
feature_names = vectorizer.get_feature_names()

df = pandas.DataFrame(tfidf_output.T.todense(), 
                  index=feature_names, 
                  columns=['idf_weights']
                  )

df = df.sort_values(by=['idf_weights'], ascending=False)

print (df.head(10))
