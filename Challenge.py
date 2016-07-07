# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 09:39:22 2016

@author: Danius
"""
import collections

wordlist = sorted(list(set([word.strip().lower() for word in open('words','r')])))

def signature(word):
    return ''.join(sorted(word))

anagramlist = collections.defaultdict(list)
for word in wordlist:
    anagramlist[signature(word)].append(word)

def anagram_fast(word):
    return anagramlist[signature(word)]

wlengthlist = collections.defaultdict(list)
for word in wordlist:
    wlengthlist[len(word)].append(word)

anagramlenlist = collections.defaultdict(list)
for length,words in wlengthlist.items():
    anagramlenlist[length] = {word:anagram_fast(word) for word in words if len(anagram_fast(word)) > 1}

anagramctlist = collections.defaultdict(list)
for length,words in wlengthlist.items():
    anagramctlist[length] = sum(len(anagram_fast(word))-1 for word in words if len(anagram_fast(word)) > 1)/2
    
print('I made a change')