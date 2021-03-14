import nltk
#measure how often two words co-occur
comm_success = '/Users/duanran/Desktop/commercially_successful_group_all_lyrics.txt'
comm_success_open = open(comm_success, 'r', errors='ignore')
comm_success_corpus = comm_success_open.read()

tokens = nltk.word_tokenize(comm_success_corpus)
#building unigram FD
unigram_fd = nltk.FreqDist(tokens)
#building bigram FD
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
#calculate collocation
collocation = []
for w1, w2 in bigram_fd:
    if unigram_fd[w1] > 10 and unigram_fd[w2] > 10: 
        pw1 = unigram_fd[w1] / unigram_fd.N()
        pw2 = unigram_fd[w2] / unigram_fd.N()
        pw1w2 = bigram_fd[(w1,w2)] / bigram_fd.N()
        #(score,(w1,w2))
        score = pw1w2/ (pw1*pw2)
        collocation.append((score,(w1,w2)))
collocation.sort()
print("-----------comm success group-------------")
for score, colloc in collocation[-30:]:#30 highest collocations
    print(score, colloc)


crit_acclaim = '/Users/duanran/Desktop/critically_acclaimed_group_all_lyrics.txt'
crit_acclaim_open = open(crit_acclaim, 'r', errors='ignore')
crit_acclaim_corpus = crit_acclaim_open.read()

tokens = nltk.word_tokenize(crit_acclaim_corpus)
#building unigram FD
unigram_fd = nltk.FreqDist(tokens)
#building bigram FD
bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
#calculate collocation
collocation = []
for w1, w2 in bigram_fd:
    if unigram_fd[w1] > 10 and unigram_fd[w2] > 10: 
        pw1 = unigram_fd[w1] / unigram_fd.N()
        pw2 = unigram_fd[w2] / unigram_fd.N()
        pw1w2 = bigram_fd[(w1,w2)] / bigram_fd.N()
        #(score,(w1,w2))
        score = pw1w2/ (pw1*pw2)
        collocation.append((score,(w1,w2)))
collocation.sort()
print("------------crit acclaim group-----------")
for score, colloc in collocation[-30:]:#30 highest collocations
    print(score, colloc)
