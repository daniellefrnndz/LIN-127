from sklearn.feature_extraction.text import TfidfVectorizer
import pandas

# Read lyrics file, separate each song by using split
# with the divider as an argument.
lyrics_file = 'C:\\Users\\Eric\\Desktop\\data\\commercially_successful_group_all_lyrics.txt'
lyrics_file_open = open(lyrics_file, 'r', errors='ignore')       
corpus = lyrics_file_open.read()
corpus = corpus.split('###############################################')

# Convert the collection of raw documents into a matrix
# of TF-IDF features.
# Strips any accented characters, removes English stop words,
# tokenizes the text, uses add-one smoothing, and looks
# only at ngrams of n = 1.
vectorizer = TfidfVectorizer(input='content',
                             strip_accents='ascii', 
                             analyzer='word', 
                             stop_words='english', 
                             use_idf=True, 
                             smooth_idf=True,
                             sublinear_tf=True, 
                             ngram_range=(1,1)
                             )

# Fits the corpus to the vectorizer to create 
# the feature matrix
tfidf_vectors = vectorizer.fit_transform(corpus)

# Display the dimensions on the matrix
# (x, y) = x songs, y token types (features)
print("Dimensions of feature matrix: ", tfidf_vectors.shape)

# We want the features for each song, so
# save how many there are
number_of_songs = tfidf_vectors.shape[0]

# Need the feature names as well
feature_names = vectorizer.get_feature_names()

for i in range(number_of_songs):

    # Find the vector for the current song
    tfidf_output = tfidf_vectors[i]

    # Create a dataframe
    # x = feature name
    # y = TFIDF weights
    df = pandas.DataFrame(tfidf_output.T.todense(), 
                    index=feature_names, 
                    columns=['tfidf_weights']
                    )

    # Sort in descending order so highest weights are
    # at the top of the column.
    df = df.sort_values(by=['tfidf_weights'], ascending=False)

    # Print top 3 highest weights for each song
    print(df.head(3))
