#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:36:52 2018

@author: dmitriy
"""

import pymorphy2
import pandas as pd
from helper_fun import *
morph = pymorphy2.MorphAnalyzer()



from pymystem3 import Mystem
mystem = Mystem()


def  get_part_of_speech(word):
    an =  mystem.analyze(word)
    z = an[0]['analysis'][0]['gr']
    pos = z.split(',')[0]
    return pos

def return_array_pos(words):
    result = []
    for i in words:
        result.append(get_part_of_speech(i))
    return result

def  test():
    
    text = 'Как насчёт небольшого стемминга'
    lemmas = mystem.lemmatize(text)
    print(''.join(lemmas))
    
    an = mystem.analyze("Дом")
    
    print an['gr']

def do_main():    
    text = get_one_text('berdaev.txt')
    res = clean_text(text)
    words = text.split(' ')
    words_2 = []
    for i in words:
        if (i != ''):
            words_2.append(i)
    
    
            
    
    



