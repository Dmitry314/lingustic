#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:56:59 2018

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





def lemming(res):
    tmp = res.split(' ')
    my_dict = {}
    for i in tmp:
        if(i != ''):
            word = morph.parse(i)[0]
            word = word.normal_form
            if(my_dict.get(word, -1) == -1):
                my_dict[word] = 1
            else:
                my_dict[word] += 1
    
    return my_dict

import numpy as np

def plot_dist_of_words(my_list):
    tmp = []
    for i in my_list:
        tmp.append(i[1])
    tmp1 = tmp[:100]
    tmp2 = tmp[100:]
    tmp1= pd.DataFrame(tmp1)
    tmp2 = pd.DataFrame(tmp2)
    tmp1.plot(kind = 'hist', bins = 20)
    tmp2.plot(kind = 'hist', bins = 20)    

def get_number_words(my_dict):
    s = 0
    for i in my_dict.keys():
        s = s + my_dict[i]
    
    return s

def get_unique_words(my_dict):
    s = 0
    for i in my_dict.keys():
        s += 1
    
    return s


def get_ratio(dict1, dict2):
    a1 = get_unique_words(dict1)
    a2 = get_unique_words(dict2)
    
    return float(a1 + 0.0001) / a2


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
    

def get_omonims_number(res):
    tmp = res.split(' ')
    
    n = 0
    for i in tmp:
        word = morph.parse(i)
        if(len(word) > 1):
            n+=1
        
    
    return n, len(tmp)
  


def get_omonims_number_dist(res):
    tmp = res.split(' ')
   
    tmp2 = []
    for i in tmp:
        word = morph.parse(i)
        tmp2.append(len(word))
    tmp2.sort()
    df = pd.DataFrame(tmp2[:int(len(tmp2))])
    df = df[df[0] > 1]
    df.plot.hist(bins  = 40)
    df = df[df[0]< 10] 
    print(df[0].mean())
    return df

def get_unknown_words(res):
    tmp = res.split(' ')
   
    tmp2 = {}
    for i in tmp:
        word = morph.parse(i)
        if(str(word[0]).find('Unknown')!=-1):
            tmp2[i] = 1
    return tmp2
    

    
def get_omon_max(dict2):
    answ = 0
    result = ''
    for i in dict2.keys():
        if(len(str(morph.parse(i))) > 1):
            if(dict2[i] > answ):
                answ = dict2[i]
                
                result = i 
    return result, answ
    

def main_job():
    list_of_books = ['berdaev.txt', 'game_of_biser.txt', 'head_of_douel.txt',
                     'humor.txt', 'kristi_dog_which_does_not_bark.txt', 
                     'nauchpop.txt', 'war_and_peace.txt']
    position = 3
    data = get_one_text(list_of_books[position])
    res = clean_text(data)
    
    
    
    my_dict1 = get_dict(res)
    my_list = get_list(my_dict1)
      
    
    
    
    my_dict2 = lemming(res)
    my_list2 = get_list(my_dict1)  
    
    print(len(res.split(' '))) #общее число словоупотреблений
    print(get_unique_words(my_dict1)) #число уникальных словоформ
    print(get_unique_words(my_dict2)) #число уникальных лемм
    
    print float(get_unique_words(my_dict2))/len(res.split(' ')) #отношение числа уникальных лемм ко всему
    
    
    plot_dist_of_words(my_list) #распределение по частоте употребления
    
    unknown_words = get_unknown_words(res) #неизвестные слова
    z = 0
    for i in unknown_words.keys():
        print(i)
        z = z + 1
        if(z > 20):
            break
    print(len(unknown_words))
    
    df = get_omonims_number_dist(res) #распределение омонимов по частотам
    n_omon, n_total = get_omonims_number(res)
    print((n_omon + 0.1)/n_total) # доля омонимов в тексте
    
    print df[0].mean()
    print df[0].max()
    
    
   
    

    
    
    





