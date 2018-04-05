#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:36:52 2018

@author: dmitriy
"""

import pymorphy2
import pandas as pd
from helper_fun import *
from helper_fun import clean_text
from wrapper import *
morph = pymorphy2.MorphAnalyzer()



from pymystem3 import Mystem
mystem = Mystem()
   

#IT is a trap!! the Noun in stem is S!!!!

def find_ANAN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'A' and
           aow[i+1].part_of_speech == 'S' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res

def find_AADVAN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'A' and
           aow[i+1].part_of_speech == 'ADV' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res

def find_VAAN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'V' and
           aow[i+1].part_of_speech == 'A' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res

def find_ANUMADJAN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'ANUM' and
           aow[i+1].part_of_speech == 'ADJ' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res

def find_ANUMAAN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'ANUM' and
           aow[i+1].part_of_speech == 'A' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res

def find_PRAAN(aow, word_2):
    res = []
    list_of_prep = [u"в", u'из', u'под',u'на', u'вдоль']
    for i in range(0, len(word_2) - 4):
        if(aow[i].word in set(list_of_prep) and
           aow[i+1].part_of_speech == 'A' and
           aow[i+2].part_of_speech == 'A' and
           aow[i+3].part_of_speech == 'S'):
            res.append((word_2[i], word_2[i+1], word_2[i+2], word_2[i+3]))
    
    return res
    

def find_AN(aow, word_2):
    res = []
    for i in range(0, len(word_2) - 4):
        if(aow[i].part_of_speech == 'A' and
           aow[i+1].part_of_speech == 'S'):
      
            res.append((word_2[i], word_2[i+1]))
    
    return res


def test_and_look(aow):
    s = 0
    for i in range(0, len(aow)):
        print(aow[i].part_of_speech)
        if(s > 1000):
            break
            s+=1
            
from tqdm import tqdm           
def do_main(title = 'berdaev.txt'):    
    text = get_one_text(title)
    res = clean_text(text)
    words = res.split(' ')
    words_2 = []
    for i in words:
        if (i != '' and not ':' in set(i)):
            words_2.append(i)
    
    
    aow = [] #array_of_wrappers
    for i in tqdm(range(len( words_2))):
        aow.append(wrapper(words_2[i]))
   
    anan = pd.DataFrame(find_ANAN(aow, words_2))
    vaan = pd.DataFrame(find_VAAN(aow, words_2))
    aadvan = pd.DataFrame(find_AADVAN(aow, words_2))
    anumaan = pd.DataFrame(find_ANUMAAN(aow, words_2))
    praan = pd.DataFrame(find_PRAAN(aow, words_2))
    
    
    anan.to_csv(title[:-3] + 'ANAN' + '.csv', encoding = 'utf-8')
    vaan.to_csv(title[:-3] + 'VAAN' + '.csv',  encoding = 'utf-8')
    aadvan.to_csv(title[:-3] + 'AADVAN' + '.csv', encoding = 'utf-8')
    anumaan.to_csv(title[:-3] + 'VAAN' + '.csv',  encoding = 'utf-8')
    praan.to_csv(title[:-3] + 'AADVAN' + '.csv', encoding = 'utf-8')

list_of_books = ['berdaev.txt', 'game_of_biser.txt', 'head_of_douel.txt',
                     'humor.txt', 'kristi_dog_which_does_not_bark.txt', 
                     'nauchpop.txt', 'war_and_peace.txt']

for i in list_of_books:
    do_main(i)
    
    
    
    
    















