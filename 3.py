# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:59:50 2017

@author: ZHENGHAN ZHANG
"""

import helpers

import random
usrdict = {}
i=1
while i <=100:
    key = helpers.genkey()
    if key in usrdict:
        continue
    usrdict[key] = random.randint(0,9)
    i+=1
print(usrdict)
helpers.ishundred(usrdict)

inverted_dictionary={}

for j in list(set(usrdict.values())):
    m=[]
    for i in usrdict:    
        if usrdict[i]==j:
            m.append(i)
    inverted_dictionary[j]=m    
print(inverted_dictionary)