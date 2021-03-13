import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas


# '/home/dfer/project/commercially_successful_group_all_lyrics.txt'
lyrics_file = 'C:\\Users\\Eric\\Desktop\\data\\commercially_successful_group_all_lyrics.txt'          # commercially successful group
lyrics_file_open = open(lyrics_file, 'r', errors='ignore')             

corpus = lyrics_file_open.read()
corpus = nltk.word_tokenize(corpus)

vectorizer = TfidfVectorizer()
vectorizer = TfidfVectorizer(input={'lyrics_file_open'}, 
                             strip_accents='ascii', 
                             analyzer='word', 
                             stop_words={'english'}, 
                             use_idf=True, 
                             smooth_idf=True, 
                             ngram_range=(1,3)
                             )

vectors = vectorizer.fit_transform(raw_documents=corpus)

first_vector_tfidfvectorizer=vectors[0]

df = pandas.DataFrame(first_vector_tfidfvectorizer.T.todense(), 
                  index=vectorizer.get_feature_names(), 
                  columns=['idf_weights']
                  )

df = df.sort_values(by=['idf_weights'], ascending=False)

print (df.head(25))