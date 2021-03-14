import nltk

comm_success = '/Users/duanran/Desktop/commercially_successful_group_all_lyrics.txt'
comm_success_open = open(comm_success, 'r', errors='ignore')
comm_success_corpus = comm_success_open.read()
comm_success_corpus = comm_success_corpus.split('###############################################')

first_sample = ['I', 'me', 'my', 'mine', 'myself', 'we', 'us', 'our', 'ours', 'ourselves']
first = []
for i in range (10):
    first.append(0)
second_sample = ['you', 'your', 'yours', 'yourself', 'yourselves']
second = [0,0,0,0,0]
third_sample = ['he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'they',
                'them', 'their', 'theirs', 'themselves', 'it', 'its', 'itself']
third = []
for i in range (16):
    third.append(0)
gender_neutral_sample = ['zie','sie','ey','ve','tey','e','zim','sie','em','ver','ter',
                         'zir','hir','eir','vis','tem','eir','zis','hirs','eirs','vers',
                         'ters','eirs','zieself','hirself','eirself','verself','terself',
                         'emself']
gender_neutral = []
for i in range (29):
    gender_neutral.append(0)
    
for i in comm_success_corpus:
    list = nltk.word_tokenize(i)
    for j in list:
        for a in range(len(first_sample)):
            if j == first_sample[a]: first[a]+=1
        for b in range(len(second_sample)):
            if j == second_sample[b]: second[b]+=1
        for c in range(len(third_sample)):
            if j == third_sample[c]: third[c]+=1
        for d in range(len(gender_neutral_sample)):
            if j == gender_neutral_sample[d]: gender_neutral[d]+=1

print('comm success group\n','1st person:', first,'\n', '2nd person:', second,'\n','3rd person:',third)
print('first pronouns:', sum(first))
print('second pronouns:', sum(second))
print('third pronouns:', sum(third))
print('gender neutral pronouns:', sum(gender_neutral))
# subject: I we you he she they it
subject_pronouns = first[0]+first[5]+second[0]+third[0]+third[4]+third[8]+third[13]
print('subject pronouns:', subject_pronouns)
# object: me you him her it us them
object_pronouns = first[1]+first[6]+second[0]+third[1]+third[5]+third[9]+third[13]
print('object pronouns:', object_pronouns)
# posessive: mine yours his hers its ours theirs
posessive_pronouns = first[3]+first[8]+second[2]+third[2]+third[6]+third[11]+third[14]
print('posessive pronouns:', posessive_pronouns)
# reflexive: myself yourself himself herself itself ourselves yourselves themselves
reflexive_pronouns = first[4]+first[9]+second[3]+second[4]+third[3]+third[7]+third[12]+third[15]
print('reflexive pronouns:', reflexive_pronouns)
print('\n')

crit_acclaim = '/Users/duanran/Desktop/critically_acclaimed_group_all_lyrics.txt'
crit_acclaim_open = open(crit_acclaim, 'r', errors='ignore')
crit_acclaim_corpus = crit_acclaim_open.read()
crit_acclaim_corpus = crit_acclaim_corpus.split('###############################################')
first = []
for i in range (10):
    first.append(0)
second = [0,0,0,0,0]
third = []
for i in range (16):
    third.append(0)
gender_neutral = []
for i in range (29):
    gender_neutral.append(0)
    
for i in crit_acclaim_corpus:
    list = nltk.word_tokenize(i)
    for j in list:
        for a in range(len(first_sample)):
            if j == first_sample[a]: first[a]+=1
        for b in range(len(second_sample)):
            if j == second_sample[b]: second[b]+=1
        for c in range(len(third_sample)):
            if j == third_sample[c]: third[c]+=1
        for d in range(len(gender_neutral_sample)):
            if j == gender_neutral_sample[d]: gender_neutral[d]+=1

print('crit acclaim group\n','1st person:', first,'\n', '2nd person:', second,'\n','3rd person:',third)
print('first pronouns:', sum(first))
print('second pronouns:', sum(second))
print('third pronouns:', sum(third))
print('gender neutral pronouns:', sum(gender_neutral))
subject_pronouns = first[0]+first[6]+second[0]+third[0]+third[4]+third[8]+third[13]
print('subject pronouns:', subject_pronouns)
object_pronouns = first[1]+first[6]+second[0]+third[1]+third[5]+third[9]+third[13]
print('object pronouns:', object_pronouns)
posessive_pronouns = first[3]+first[8]+second[2]+third[2]+third[6]+third[11]+third[14]
print('posessive pronouns:', posessive_pronouns)
reflexive_pronouns = first[4]+first[9]+second[3]+second[4]+third[3]+third[7]+third[12]+third[15]
print('reflexive pronouns:', reflexive_pronouns)
