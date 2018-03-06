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
    number_of_words = 0
    dictonary_of_all_words = {}
    
    for i in tqdm(range(2, num)):
        if(i < 10):
            filename = base_filename + '0' + str(i) + '.sgm'
        else:
            filename = base_filename + str(i) + '.sgm'
        data = get_one_text(filename)
        
        res = clean_text(data)
        number_of_words += get_num_of_words(res)
        
        answer = get_bi_grams(res)
        dictonary_of_one_dataset = get_dict(res)
        
        for i in dictonary_of_one_dataset.keys():
             if(dictonary_of_all_words.get(i, -1) == -1):
                dictonary_of_all_words[i] = dictonary_of_one_dataset[i]
             else:
                dictonary_of_all_words[i] += dictonary_of_one_dataset[i]
        
        '''
        This function is awful and must be rewritten
        '''        
        
        
        
        for i in answer.keys():
            if(total_answer.get(i, -1) == -1):
                total_answer[i] = answer[i]
            else:
                total_answer[i] += answer[i]
                

    return total_answer, number_of_words, dictonary_of_all_words 




def get_word2Iword1_not_smooth(word1, word2, dict_of_bi_grams):
    
    a = 0
    b = 0
    
    for i in dict_of_bi_grams.keys():
        if (i.split(' ')[0] == word1):
            a+=1
        
        
        if (i.split(' ')[0] == word1 and i.split(' ')[1] == word2):
            b+=1
    
    return float(b) / a


def get_word2Iword1_smooth(word1, word2, dict_of_bi_grams, num_of_words):
    
    a = 0
    b = 0
    
    for i in dict_of_bi_grams.keys():
        if (i.split(' ')[0] == word1):
            a+=1
        
        
        if (i.split(' ')[0] == word1 and i.split(' ')[1] == word2):
            b+=1
    
    return float(b + 1)/(a + num_of_words)    




def get_probab_of_word(word, dict_of_all_words,  num_of_words):
    return float(dict_of_all_words[word]) / num_of_words


def get_chain_prob_not_smooth(text, dict_of_all_words, dict_of_bi_grams, num_of_words):
    tmp = text.split(' ')
    
    answer = get_probab_of_word(tmp[0], dict_of_all_words, num_of_words )
    
    for i in range(1, len(tmp)):
        
        answer = answer * get_word2Iword1_not_smooth(tmp[i-1], tmp[i], dict_of_bi_grams)
        
    return answer

def get_chain_prob_smooth(text, dict_of_all_words, dict_of_bi_grams, num_of_words):
    tmp = text.split(' ')
    
    answer = get_probab_of_word(tmp[0], dict_of_all_words, num_of_words )
    
    for i in range(1, len(tmp)):
        
        answer = answer * get_word2Iword1_smooth(tmp[i-1], tmp[i], dict_of_bi_grams, number_of_words)
        
    return answer

from numpy import roots
def get_perpleksia(n, num_of_words):
    return float(1)/(n**(float(1)/num_of_words))

def do_job_for_report():
    
    total_answer, number_of_words, dictonary_of_all_words = get_reuturs_data()
    
    most_bi_grams = get_most_bi_grams(total_answer)
    my_list = ['the united states has', 'accused japan of reneging on the', 
    'semiconductor pact by failing',  'to stop the flow', 'of cutprice japanese chips',  
    'to asian markets', 'washington has threatened to']
    
    for i in my_list:
        print(i)
        prob = get_chain_prob_not_smooth(i, dictonary_of_all_words,  total_answer, 
                             number_of_words )
        print('probability: ', prob,  ' perpleksia: ', get_perpleksia(prob, len(i)))
  
    
    
    
    #phrases taken from Jane Eyre
    my_list_2 = ['large face the under jaw', 'being much developed and very solid',
                 'her brow was low', 'her chin large and prominent', 'mouth and nose sufficiently regular']
    
    for i in my_list_2:
        print(i)
        

        
        
        prob = get_chain_prob_smooth(i, dictonary_of_all_words,  total_answer, 
                             number_of_words )
        
        print('probability: ', prob,  ' perpleksia: ', get_perpleksia(prob, len(i)))
 

def get_bi_grams_simple():
    
    list_of_books = ['berdaev.txt', 'game_of_biser.txt', 'head_of_douel.txt',
                     'humor.txt', 'kristi_dog_which_does_not_bark.txt', 
                     'nauchpop.txt', 'war_and_peace.txt']
    position = 0
    
    data = get_one_text(list_of_books[position])
    res = clean_text(data)
    lbg = get_bi_grams(res)
    ltg = get_tri_grams(res)
    
    #lbg = get_most_bi_grams(lbg)
    #ltg = get_most_bi_grams(ltg)
    return lbg, ltg

from copy import deepcopy

def generate_bred(start_word, dict_of_bi_grams, number_of_words = 10):
    answer = []
    answer.append(start_word)
    current = start_word
    for i in tqdm(range(number_of_words)):
        tmp =  []
        prob = []
        tmp2 = []
        norm = 0
        for j in dict_of_bi_grams.keys():
            if(j.split(' ')[0] == current):
                tmp2.append((j, dict_of_bi_grams[j]))
                norm += dict_of_bi_grams[j]
        
        for j in range(0, len(tmp2)):
            tmp.append(tmp2[j][0].split(' ')[1])
            prob.append(float(tmp2[j][1]) / norm)
        
        an = np.random.choice(tmp, p = prob)
        answer.append(an)
        current = an
    return answer


def generate_bred_tri(start_word, second_start_word, dict_of_tri_grams, number_of_words = 10):
    answer = []
    answer.append(start_word)
    answer.append(second_start_word)
    current1 = start_word
    current2 = second_start_word
    for i in tqdm(range(number_of_words)):
        tmp =  []
        prob = []
        tmp2 = []
        norm = 0
        for j in dict_of_tri_grams.keys():
            if(j.split(' ')[0] == current1 and j.split(' ')[1] == current2):
                tmp2.append((j, dict_of_tri_grams[j]))
                norm += dict_of_tri_grams[j]
        
        for j in range(0, len(tmp2)):
            tmp.append(tmp2[j][0].split(' ')[2])
            prob.append(float(tmp2[j][1]) / norm)
        
        an = np.random.choice(tmp, p = prob)
        answer.append(an)
        current1 = current2
        current2 = an
    return answer

bred = generate_bred_tri(u'глубину', u'эту', ltg, 100)


start_word = u'он'
dict_of_bi_grams = lbg
i = 0

                
                
        
        
        
        
        
        
        
            
    
    

