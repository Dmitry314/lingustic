#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 19:06:52 2018

@author: dmitriy
"""

from pymystem3 import Mystem
mystem = Mystem()

def see_at_diff_casses():
    
    a2 = mystem.analyze("в")
    a3 = mystem.analyze("красивого")
    a4 = mystem.analyze("бежать")
    a5 = mystem.analyze("стих")
    a6 = mystem.analyze("стали")
    a7 = mystem.analyze("бежавший")
    a8 = mystem.analyze("стать")
    a9 = mystem.analyze("красив")
    a10 = mystem.analyze("сделано")
    a11 = mystem.analyze("быстро")
    a12 = mystem.analyze("первый")
    a13 = mystem.analyze("второй")





class wrapper:
    '''
    mystem is awful.
    the important data data is returened in a string.
    You have to parse the string. OK.
    For every part of speech there are lots of formats of a string.
    It is quite difficult.
    wtf?
    '''
    
    
    def __init__(self, word):
        self.know_nothing = False
        self.word = word
        self.part_of_speech = None
        self.infinitiv = False
        
        
        an = mystem.analyze(word)
       
        if(an[0].get('analysis', -1) == -1):
            self.know_nothing = True
        else:
            z = an[0]['analysis']
        
        if(self.know_nothing == False and len(z) == 0):
            self.know_nothing = True
        
        
        if(self.know_nothing == False and z[0].get('gr', -1) == -1):
            self.know_nothing = True
            
        if(self.know_nothing == False and len(z[0]['gr']) < 3 ):
            self.know_nothing = True
        if(self.know_nothing == False):
            zz = z[0]['gr']
            
            if(zz[0] == 'S'):
                self.case = []
                self.noun_number = []
                self.part_of_speech = 'S'
                tmp = zz.split('=')    
                
                if(len(tmp) > 2):
                    print(zz)
                    
                
                
                tmp2 = tmp[1].split('|')
                tmp3 = []
                for j in range(0, len(tmp2[0])):
                    if(tmp2[0][j]!='(' and tmp2[0][j]!=')' ):
                        if(tmp2[0][j] == ','):
                            break
                        tmp3.append(tmp2[0][j])
                
                self.case = "".join(tmp3)
            
            
            if(zz[0] == 'V'):
                self.part_of_speech = 'V'
                if(zz.find(u'инф')!= -1):
                    self.infinitiv = True
            
            
            if(zz[0] == 'A' and not (zz[1] =='D'and zz[2] == 'V')):
                self.part_of_speech = 'A'
                
                if(zz.find(u'кр')!= -1):
                    self.case = 'short'
                else:
                    tmp = zz.split('=')    
                    
                    if(len(tmp) > 2):
                        print(zz)
                        
                    
                    
                    tmp2 = tmp[1].split('|')
                    tmp3 = []
                    for j in range(0, len(tmp2[0])):
                        if(tmp2[0][j]!='(' and tmp2[0][j]!=')' ):
                            if(tmp2[0][j] == ','):
                                break
                            tmp3.append(tmp2[0][j])
                    
                    self.case = "".join(tmp3)
            
            
            if(zz[0] == 'A' and zz[1] =='D'and zz[2] == 'V'):
                self.part_of_speech = 'ADV'
                
            
            
            if(zz[0:4] == 'ANUM'):
                self.part_of_speech = 'ANUM'
                

            
            
            
            
            
                    
                    
            
                
            
        
        
        
        
        
        