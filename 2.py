# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:19:12 2017

@author: ZHENGHAN ZHANG
"""

#ask the user for a string

s=input('Enter a string: ')
alphabets=list(set(s))
dict1={}
for i in alphabets:
    m=0
    for j in s:
        if i==j:
            m+=1
    dict1[i]=m
for i in sorted(dict1):
    print(i,dict1[i],sep='->')    