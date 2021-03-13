import pandas as pd
import glob

dataset = []

from sklearn.feature_extraction.text import TfidfVectorizer
lyrics_files = glob.glob('/home/dfer/project/commercially_successful_group_all_lyrics/*.txt')          # commercially successful group


for file in lyrics_files:
    lyrics_file = open(file, 'r')             
    lyrics_text = lyrics_file.read()         
    lyrics_tokens = nltk.word_tokenize(lyrics_text)    

dataset = dataset + lyrics_tokens

tfIdfVectorizer = TfidfVectorizer(use_idf=True)
tfIdf = tfIdfVectorizer.fit_transform(dataset)
df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)
print (df.head(25))


