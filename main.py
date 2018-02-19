#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:56:59 2018

@author: dmitriy
"""


import pymorphy2
import pandas as pd
morph = pymorphy2.MorphAnalyzer()

def get_one_text():
    with open('head_of_douel.txt') as f:
        read_data = f.read()
    
    return read_data



def clean_text(data):
    res = []
    for i in data:
        if not i in set('!@#$%^&*()_+}{[]?.,/'):
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
        print(i)
        print(my_dict[i])
        tmp.append((i, my_dict[i]))
        
    return tmp




