#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 21:21:36 2018

@author: dmitriy
"""


import pymorphy2
import pandas as pd
morph = pymorphy2.MorphAnalyzer()

def get_one_text(my_file):
    with open(my_file) as f:
        read_data = f.read()
    
    return read_data




def clean_text(data):
    res = []
    for i in data:
        if not i in set('!@#$%^&*()_+}{[]?.,/-\"'):
            if(i == '\n'):
                res.append(' ')
            else:
                res.append(i)
    
    res = "".join(res)
    res = res.decode('utf-8').lower()
    
    return res


def get_dict(res):
    tmp = res.split(' ')
    my_dict = {}
    for i in tmp:
        if(i != ''):
            if(my_dict.get(i, -1) == -1):
                my_dict[i] = 1
            else:
                my_dict[i] += 1
    
    return my_dict




def get_list(my_dict):
    tmp = []
    for i in my_dict.keys():
        
        
        tmp.append((i, my_dict[i]))
        tmp.sort(key = lambda w: w[1], reverse = True)
    return tmp
import pymorphy2
import pandas as pd
morph = pymorphy2.MorphAnalyzer()

def get_one_text(my_file):
    with open(my_file) as f:
        read_data = f.read()
    
    return read_data




def clean_text(data):
    res = []
    for i in data:
        if not i in set('!@#$%^&*()_+}{[]?.,/-\"'):
            if(i == '\n'):
                res.append(' ')
            else:
                res.append(i)
    
    res = "".join(res)
    res = res.decode('utf-8').lower()
    
    return res


def get_dict(res):
    tmp = res.split(' ')
    my_dict = {}
    for i in tmp:
        if(i != ''):
            if(my_dict.get(i, -1) == -1):
                my_dict[i] = 1
            else:
                my_dict[i] += 1
    
    return my_dict




def get_list(my_dict):
    tmp = []
    for i in my_dict.keys():
        
        
        tmp.append((i, my_dict[i]))
        tmp.sort(key = lambda w: w[1], reverse = True)
    return tmp


import numpy as np

def get_omonims(dict1):
    res = []
    for i in dict1.keys():
        res.append((i, len(morph.parse(i))))
    
    res.sort(key = lambda w  : w[1], reverse = True)
    return res



def get_word_length_dist(res):
    tmp = res.split(' ')
    tmp2 = []
    for i in tmp:
        tmp2.append(len(i))
    
    tmp2.sort()
    tmp2 = tmp2[int(len(tmp2)*0.9):]
    
    df = pd.DataFrame(tmp2)
    df.plot.hist()





def get_num_of_words(res):
    n = 0
    tmp = res.split(' ')
    for i in tmp:
        if(i !=''):
           n+=1
        return n


def get_bi_grams(res):

    tmp = res.split(' ')
    clean_tmp  = []
    answer = {}
    
    for i in range(0, len(tmp)):
        if(tmp[i] != ''):
            clean_tmp.append(tmp[i])
    
    
    for i in range(0, len(clean_tmp) - 2):
        if(answer.get(clean_tmp[i] + ' ' + clean_tmp[i+1], -1) == -1):
            answer[clean_tmp[i] + ' ' + clean_tmp[i+1] ] = 1
        else:
            answer[clean_tmp[i] + ' ' + clean_tmp[i+1] ] +=1
            
    return answer



def get_most_bi_grams(answer):
    a = []
    for key in answer.keys():
        a.append((key, answer[key]))
    
    a.sort(key = lambda w : w[1], reverse = True )
    return a



def get_tri_grams(res):
    tmp = res.split(' ')
    clean_tmp  = []
    answer = {}
    
    for i in range(0, len(tmp)):
        if(tmp[i] != ''):
            clean_tmp.append(tmp[i])
    
    
    for i in range(0, len(clean_tmp) - 2):
        if(answer.get(clean_tmp[i] + ' ' + clean_tmp[i+1] + ' ' + clean_tmp[i+2], -1) == -1):
            answer[clean_tmp[i] + ' ' + clean_tmp[i+1] + ' ' + clean_tmp[i+2] ] = 1
        else:
            answer[clean_tmp[i] + ' ' + clean_tmp[i+1] + ' ' + clean_tmp[i+2] ] +=1
    return answer



list_of_books = ['berdaev.txt', 'game_of_biser.txt', 'head_of_douel.txt',
                 'humor.txt', 'kristi_dog_which_does_not_bark.txt', 
                 'nauchpop.txt', 'war_and_peace.txt']
position = 0

data = get_one_text(list_of_books[position])
res = clean_text(data)



my_dict1 = get_dict(res)

from tqdm import tqdm
def  get_reuturs_data(num = 15):
    
    base_filename = 'reuters/reut2-0'
    total_answer = {}
    for i in tqdm(range(2, num)):
        if(i < 10):
            filename = base_filename + '0' + str(i) + '.sgm'
        else:
            filename = base_filename + str(i) + '.sgm'
        data = get_one_text(filename)
        res = clean_text(data)
        
        answer = get_bi_grams(res)
        for i in answer.keys():
            if(total_answer.get(i, -1) == -1):
                total_answer[i] = answer[i]
            else:
                total_answer[i] += answer[i]
                
    most_bi_grams = get_most_bi_grams(total_answer)
        

def get_dict_contained_word(total_answer, word):
    for key in total_answer.keys



 
    



    