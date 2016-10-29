# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:56:20 2016

@author: Sayak
"""

word = open('C:\\Users\\acer\\Downloads\\Exercise Files\\Ch3\\03_03\\words.txt' , 'r')
wordlist = word.readlines()
word_small = [word.lower().strip() for word in wordlist]
words_unique = list(set(word_small))
words_unique.sort()
def signature(word):
    return ''.join(sorted(word))
def anagram(myword):
   return [word for word in words_unique if signature(word) == signature(myword)] 
import collections as col
words_bysig = col.defaultdict(list)
for word in words_unique:
   words_bysig[signature(word)].append(word)
#print(words_bysig)
def anagram_fast(myword):
    return words_bysig[signature(myword)]
#print(anagram_fast("dictionary"))
anagram_all = {word: anagram_fast(word) for word in words_unique if len(anagram_fast(word)) > 1}


words_bylength = col.defaultdict(list)
for word in words_unique:
    words_bylength[len(word)].append(word) 

anagrams_bylength = {}
for length, words in words_bylength.items():
    anagrams_bylength[length] =  sum(len(anagram_fast(word)) - 1  for word in words if len(anagram_fast(word)) > 1)/2
print (anagrams_bylength)