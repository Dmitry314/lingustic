#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 14:09:27 2018

@author: dmitriy
"""

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