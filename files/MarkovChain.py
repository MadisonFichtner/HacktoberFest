import pandas as pd
from numpy.random import choice
import numpy as np

def read_file(file):
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

def make_sentence(first_word, word_count, word_dict):
    chain = [first_word]

    for i in range(word_count):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    chain = ' '.join([str(elem) for elem in chain])
    return chain

def main():
    file = read_file("test_words.txt")
    pairs = make_pairs(file)
    word_dict = make_dict(pairs)

    word_count = ""
    first_word = ""

    while first_word == "":
        first_word = input("Enter starting word: ")
        if first_word not in file:
            print("Word not found on file, try again")
            first_word = ""

    #while first_word.islower():
    #    first_word = np.random.choice(file)

    while word_count == "":
        word_count = input("Enter sentence length: ")
        word_count = int(word_count)
        if word_count <= 0:
            print("Invalid, enter value larger than 0")
            word_count = ""

    chain = make_sentence(first_word, word_count, word_dict)

    return chain

chain = main()
print(chain)
