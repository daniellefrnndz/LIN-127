import glob
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

album_filenames = glob.glob('C:\\Users\\Eric\\Desktop\\data\\comm_success\\*.txt') 

lyrics_as_list_of_strings = []

for album in album_filenames:
    album_open = open(album, 'r', errors='ignore')  
    album_read = album_open.read()
    lyrics_as_list_of_strings.append(album_read)

#'/home/dfer/project/commercially_successful_group_all_lyrics.txt'
#lyrics_file = 'C:\\Users\\Eric\\Desktop\\data\\commercially_successful_group_all_lyrics.txt' # commercially successful group

#lyrics_file_open = open(lyrics_file, 'r', errors='ignore')       

#corpus = lyrics_file_open.read()
#corpus = nltk.word_tokenize(corpus)

vectorizer = TfidfVectorizer(input='content', 
                             strip_accents='ascii', 
                             analyzer='word', 
                             stop_words='english', 
                             use_idf=True, 
                             smooth_idf=True, 
                             ngram_range=(1,1)
                             )

tfidf_vectors = vectorizer.fit_transform(lyrics_as_list_of_strings)
tfidf_output = tfidf_vectors[0]

df = pandas.DataFrame(tfidf_output.T.todense(), 
                  index=vectorizer.get_feature_names(), 
                  columns=['idf_weights']
                  )

df = df.sort_values(by=['idf_weights'], ascending=False)

print (df.head(25))
