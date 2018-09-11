# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 10:06:52 2017

@author: ZHENGHAN ZHANG
"""

#ask the user for a input
friends={}
while True:
    x=input('Please insert the name and phone number of your friend: ').split()
    if x==[]:
        break
    friends[x[0]]=x[1]

#ask the user for a name
while True:
    y=input('Please insert a name: ')
    if y=='':
        break
    if y in friends.keys():
        print(y,friends[y])
    else:
        print('Name not found')
