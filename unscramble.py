import json
from itertools import combinations
from itertools import permutations

f = open('eng_wordslist.txt', 'r')
ew = f.read()
engw = json.loads(ew)

totc = []
def getcp(word,r):

    # This finds the 'r' combinations of variable 'word' and stores in list 'listc'
    comb = [''.join(c) for c in combinations(word, r)]
    for x in comb:
        perm = [''.join(p) for p in permutations(x)]
        for y in perm:
            totc.append(y)

def tparr(word):

    r = len(word)
    for i in range(r):
        if r-i != 1:
            getcp(word, r-i)
        else:
            return

def unscramble():

    word=input("Enter the letters to Unscramble:")
    l = len(word)
    tparr(word)
    newewl = []
    for x in engw:
        w = len(x)
        if w <= l:
            newewl.append(x)
    unscl = []
    i = 0
    for each in totc:
        if each in newewl:
            unscl.append(each)
            i += 1
            print('{:>2} . {}'.format(i, each))
    print(unscl)


unscramble()
