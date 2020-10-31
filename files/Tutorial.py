import pandas as pd
from numpy.random import choice

def read_file(file):
    myfile = open(file, "r")
    content = myfile.read().splitlines()
    list = []
    for word in words(content):
        list.append(word)
    return list

def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word

def make_a_sentence(start):
    word= start
    sentence=[word]
    while len(sentence) < 30:
        next_word = choice(a = list(pivot_df.columns), p = (pivot_df.iloc[pivot_df.index ==word].fillna(0).values)[0])
        if next_word == 'EndWord':
                continue
        elif next_word in end_words:
            if len(sentence) > 2:
                sentence.append(next_word)
                break
            else :
                continue
        else :
            sentence.append(next_word)
        word=next_word
    sentence = ' '.join(sentence)
    return sentence


words = read_file("test_words.txt")
dict_df = pd.DataFrame(columns = ['lead', 'follow', 'freq'])
dict_df['lead'] = words
follow = words[1:]
follow.append('EndWord')

end_words = []
for word in words:
    if word[-1] in ['.','!','?'] and word != '.':
        end_words.append(word)
print(end_words)

dict_df['freq']= dict_df.groupby(by=['lead','follow'])['lead','follow'].transform('count').copy()

dict_df = dict_df.drop_duplicates()
pivot_df = dict_df.pivot(index = 'lead', columns= 'follow', values='freq')

sum_words = pivot_df.sum(axis=1)
pivot_df = pivot_df.apply(lambda x: x/sum_words)

sentence = make_a_sentence('sentence')
print(sentence)
