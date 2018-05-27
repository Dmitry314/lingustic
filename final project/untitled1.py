#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:29:25 2018

@author: dmitriy
"""
import string
import nltk

def clean_text_2(data):
    res = []
    for i in data:
        
        if not i in set('!@#$%^&\'*:()\x99_+}{[]?.,/-\"'):
            if(i == '\n'):
                res.append(' ')
            else:
                res.append(i)
    
    res = "".join(res)

    
    return res
    
def clean3(data):
    res = []
    a = set(string.ascii_letters)
    a.add(' ')
    for i in data:
        
        if(i == '\n'):
            res.append(' ')
        else:
            if  i in set(a):
                res.append(i)
          
    
    res = "".join(res)

    
    return res
    
import re
from helper_fun import *

def get_text(title = 'Crime.txt'):

    
    text = get_one_text(title)
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    sentences = text.split('.')
    
    
    for i in range(0, len(sentences)):
        sentences[i] = sentences[i].lstrip().rstrip()
        sentences[i] = clean3(sentences[i])
        
        sentences[i] = sentences[i].lstrip().rstrip()
        sentences[i] = clean3(sentences[i])
    
    return sentences



def find_all_names(sentences):
    answer = []
    names = {}
    for i in range(10, len(sentences)):
        Was_the_first = False
        if(len(sentences[i]) > 0):
            words = sentences[i].lstrip().split(' ')
        
            for j in range(0, len(words)):
                if(len(words[j]) > 0 and words[j].lower()!= words[j]):
                    if(Was_the_first == False):
                        Was_the_first = True
                    else:
                        
                        if(names.get(words[j], -1) == -1):
                            names[words[j]] = 1
                        else:
                            names[words[j]] += 1
                        
                        answer.append((words[j], sentences[i]))
                    
    answer = []
    for j in names.keys():
        answer.append((j, names[j]))
    
    answer.sort(key = lambda w: w[1], reverse = True)
    return answer
    

from copy import copy
from tqdm import tqdm


import nltk
from nltk.corpus import wordnet

from nltk.stem.porter import PorterStemmer

def get_synonyms(word):
    synonyms = []
    antonyms = []
     
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
     
    return synonyms,  antonyms
    


def find_all_actions(sentences, name):
    answ = []
    num_of_sentences = []
    for i in tqdm(range(0, len(sentences))):
        if(len(sentences[i]) > 0):
            
            words = sentences[i].split(' ')
            
            words = list(filter(lambda w : len(w) > 0, words))
            
            pos  = nltk.pos_tag(words)
            
            
            tmp = []
           
            is_name = False
            position = 0
            for j in range(0, len(pos)):
                
                if(pos[j][0] == name):
                    is_name = True
                    position = j+1
                    num_of_sentences.append(i)
                    break
            
            if(is_name):
                tmp.append(name)
                for j in range(position, len(pos)):
                    if('VB'  in pos[j][1]):
                        tmp.append(pos[j][0])
            
                answ.append((copy(tmp)))
    return answ, num_of_sentences



from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('maximum')


def find_all_like_verb(verb, actions, num_of_sent, sent):
    synonyms = set(get_synonyms(verb)[0])
    res = []
    for i in tqdm(range(0, len(actions))):
        for j in range(0, len(actions[i])):
            if(porter_stemmer.stem(actions[i][j]) in synonyms):
                res.append(sent[num_of_sent[i]])
          
    return res


def find_pattern_NVA(sentences):
    res = []
    for i in tqdm(range(1, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(1, len(pos) - 4):
             if('NN' in pos[j-1][0] and 'VB' in pos[j][1] and 'JJ' in pos[j+1][1] ):
                 res.append([pos[j - 1][0], pos[j][0], pos[j+1][0]])
    return res
        
        
def find_pattern_NVAAN(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(0, len(pos) - 4):
             if('VB' in pos[j][1] and 'JJ' in pos[j+1][1] and 'JJ' in pos[j+2][1] and 'NN' in pos[j+3][1] ):
                 res.append([pos[j][0], pos[j+1][0], pos[j+2][0], pos[j+3][0]])


    return res


def deal_with_he_she(sentences, name, he=True):
    
    res = []
    num_of_sentences = []
    def sent_has_name(name, sent):
        set_w = set(sent.split(' '))
        if(name in set_w):
            return True
        else:
            return False
    
    for i in tqdm(range(1, len(sentences) - 3)):
        if(sent_has_name(name, sentences[i])):
            if(he):
                j = 1
                tmp_4 = [sentences[i]]
                
                while( i + j < len(sentences) and sent_has_name('he', sentences[i + j])):
                    tmp_4.append(sentences[i+j])
                    
                    num_of_sentences.append(i + j)
                    j+=1
            res.append(copy(tmp_4))
    res = filter(lambda w: len(w)> 1, res)
          
    return num_of_sentences, res


def substitute_he_by_name(sentences, name, num_of_sentences):
    for j in num_of_sentences:
        print(j, sentences[j])
        sentences[j] = sentences[j].replace(' he ', ' ' + name + ' ')
        print(sentences[j])



text = get_text()

names = find_all_names(text)
print names[:20]
name = 'Raskolnikov' # change on any name you like

actions, num_of_sent = find_all_actions(text, name)
print len(actions)

num_of_sent, res = deal_with_he_she(text, name)

substitute_he_by_name(text, name, num_of_sent )

actions, num_of_sent = find_all_actions(text, name)
print len(actions)
verb = 'tell'
set_verb = find_all_like_verb(verb, actions, num_of_sent, text)




verb = 'go'
set_verb = find_all_like_verb(verb, actions, num_of_sent, text)


verb = 'read'
set_verb = find_all_like_verb(verb, actions, num_of_sent, text)

verb = 'do'
set_verb = find_all_like_verb(verb, actions, num_of_sent, text)

verb = 'give'
set_verb = find_all_like_verb(verb, actions, num_of_sent, text)



print set_verb[:30]




                
def find_pattern_ANAN(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(0, len(pos) - 4):
             if('JJ' in pos[j][1] and 'NN' in pos[j+1][1] and 'JJ' in pos[j+2][1] and 'NN' in pos[j+3][1] ):
                 res.append([pos[j][0], pos[j+1][0], pos[j+2][0], pos[j+3][0]])
    return res 
            
def find_pattern_NV_continues_time(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(0, len(pos) - 3):
             if('NN' in pos[j][1] and 'VB' in pos[j+1][1]):
                 if(pos[j + 1][0].lower() in (" ".join(['were', 'was', 'is', 'are']))):
                     
                     if('ing' in pos[j+2][0]):
                         if( j + 3 < len(pos) and ('NN' in pos[j+3][1] or 'JJ' in pos[j+3][1])):
                             res.append([pos[j][0], pos[j+1][0], pos[j+2][0], pos[j+3][0]])
                         else:
                             if(j + 4 < len(pos) and 'DT' in pos[j+3][1]):
                                   res.append([pos[j][0], pos[j+1][0], pos[j+2][0], pos[j+3][0], pos[j+4][0]])
                             else:
                                res.append([pos[j][0], pos[j+1][0], pos[j+2][0]])
    
    
    return res               

list_of_irreg_words =['did', 'came', 'went', 'lost']
list_of_irreg_words = set(list_of_irreg_words)




def find_pattern_NV_simple_past_time(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(0, len(pos) - 3):
             if('NN' in pos[j][1] and 'VB' in pos[j+1][1]):
                 if(pos[j+1][0][-2:] =='ed' or (pos[j+1][0] in list_of_irreg_words)):
                     
                 
                     if( j + 2 < len(pos) and ('NN' in pos[j+2][1] or 'JJ' in pos[j+2][1] or 'RB' in pos[j+2][1])):
                         res.append([pos[j][0], pos[j+1][0], pos[j+2][0]])
                     else:
                         if(j + 3 < len(pos) and 'DT' in pos[j+2][1]):
                             res.append([pos[j][0], pos[j+1][0], pos[j+2][0], pos[j+3][0]])
                         else:
                             res.append([pos[j][0], pos[j+1][0]])
                             
    return res          

from copy import copy



'''
def find_pattern_NV_continues_time_2(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         for j in range(0, len(pos) - 3):
             if('NN' in pos[j][1] and 'VB' in pos[j+1][1]):
                 if(pos[j + 1][0].lower() in (" ".join(['were', 'was', 'is', 'are']))):
                     
                     if('ing' in pos[j+2][0]):
                         tmp_i = j+3
                         tmp = []
                         tmp.append(pos[j][0])
                         tmp.append(pos[j+1][0])
                         tmp.append(pos[j+2][0])
                         while(tmp_i < len(pos) - 1 and not 'VB' in pos[tmp_i]):
                             tmp.append(pos[tmp_i][0])
                             tmp_i+=1
                        
                         res.append(copy(tmp))
    return res
                             
                             

    



def find_long_pattern_NV_continues_time(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         
         j = 0
         tmp = False
         while(j < len(pos) - 3):
             if('NN' in pos[j][1]):


def find_patter_N_V_simple_past_time(sentences):
    res = []
    for i in tqdm(range(0, len(sentences))):
         words = sentences[i].split(' ')
            
         words = list(filter(lambda w : len(w) > 0, words))
            
         pos  = nltk.pos_tag(words)
         for j in range(0, len(pos) - 3):
             if('NN' in pos[j][1] and 'VB' in pos[j+1][1]):
                 if('ed' in pos[j+1][0]):
                         if(  'NN' in pos[j+2][1]):
                             res.append([pos[j][0], pos[j+1][0], pos[j+2][0]])
                         else:
                             res.append([pos[j][0], pos[j+1][0]])
                 








                                  
    
    








def find_nv(pos):
    res = []
    for i in range(1, len(pos)):
        if(pos[i-1][1] == 'NN'  and  'V' in pos[i][1] ):
            res.append((pos[i-1], pos[i]))









'''