#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:51:05 2018

@author: dmitriy
"""


import numpy as np


def get_one_text(my_file):
    with open(my_file) as f:
        read_data = f.read()
    
    return read_data
def get_dict():
    data = get_one_text('ozgegov/oz/ozgegov.txt')
    
    res = data.split(" ")
    
    
    words = []
    
    for i in range(0, len(res)):
        if(res[i].decode('utf-8').isupper() and len(res[i]) > 2):
            words.append(i)
    
    my_dict = {}
    
    for i in range(len(words) - 1):
        key_word = []
        for j in res[words[i]]:
            if(j != '' and j != '\n' and j != ','):
                key_word.append(j)
        key_word = "".join(key_word)
        my_dict[key_word] = " ".join(res[words[i] + 1 : words[i + 1]] )
            


from nltk.corpus import wordnet    
        
# Then, we're going to use the term "program" to find synsets like so:
syns = wordnet.synsets("program")
 
# An example of a synset:
print(syns[0].name())
 
# Just the word:
print(syns[0].lemmas()[0].name())
 
# Definition of that first synset:
print(syns[0].definition())
 
# Examples of the word in use in sentences:
print(syns[0].examples())