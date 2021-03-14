import nltk
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

lyrics_file = glob.glob('/home/dfer/project/comm_success.zip/*.txt')        # commercially successful group

for file in lyrics_file:
    lyrics_file_open = open(file, 'r', errors='ignore')

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