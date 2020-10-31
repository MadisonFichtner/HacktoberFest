import pandas as pd
from numpy.random import choice
import numpy as np

def read_file(words):
    myfile = open('test_words.txt', encoding='utf8').read()
    list = myfile.split()
    return list

def make_pairs(list):
    for i in range(len(list)-1):
        yield (list[i], list[i+1])

def make_dict(pairs):
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    return word_dict

def make_sentence(first_word, end_words, word_dict):
    chain = [first_word]

    while len(chain) < 45:
        next_word = np.random.choice(word_dict[chain[-1]])
        if next_word not in end_words:
            chain.append(next_word)
            continue
        elif next_word in end_words:
            if len(chain) > 2:
                chain.append(next_word)
                break
            else:
                chain.append(next_word)


        #chain.append(np.random.choice(word_dict[chain[-1]]))

    chain = ' '.join([str(elem) for elem in chain])
    return chain

def find_ends(words):
    end_words = []
    for word in words:
        if word[-1] in ['.','!','?'] and word != '.':
            end_words.append(word)
    return end_words

def main():
    words = read_file("test_words.txt")
    pairs = make_pairs(words)
    word_dict = make_dict(pairs)
    end_words = find_ends(words)

    first_word = ""

    while first_word == "":
        first_word = input("Enter starting word: ")
        if first_word not in words:
            print("Word not found on file, try again")
            first_word = ""

    chain = make_sentence(first_word, end_words, word_dict)

    return chain

chain = main()
print(chain)
