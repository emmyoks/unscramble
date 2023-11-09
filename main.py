import json
from itertools import combinations
from itertools import permutations

''' This script only works for English words'''
file = open('eng_wordslist.txt', 'r')
eng_dict_words_str = file.read()
eng_dict_words_list = json.loads(eng_dict_words_str)
word = input("Enter the letters to Unscramble:")

def unscramble(word):
    word_length = len(word)
    potential_words_list = []
    for i in range(word_length - 1):
        possible_combinations = [''.join(c) for c in combinations(word, word_length - i)] 
        # combinations function returns a list of tuples ''.join(c) is converting each tuple to a string
        for c in possible_combinations:
            c_permutations = [''.join(p) for p in permutations(c)]
            potential_words_list.extend(c_permutations)
    reduced_eng_words_list = [] 
    for x in eng_dict_words_list:
        w = len(x)
        if w <= word_length:
            reduced_eng_words_list.append(x)
    valid_eng_word_list = []
    i = 0
    for word in potential_words_list:
        if word in reduced_eng_words_list:
            valid_eng_word_list.append(word)
            i += 1
            print(f'{i} . {word}')
    print( valid_eng_word_list )

unscramble(word)
'''Filtering and validation of english words can be restructured to increase time complexity, 
maybe hash mapping, of which validation will be done in the permutaions code block above'''
