# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:04:52 2017

@author: ZHENGHAN ZHANG
"""

import helpers
import random
#first, populate the dragons
#we start with one dragon
dragonList=[]
for i in range(300):
    mydragon={}    
    mydragon['color']=random.choice(helpers.dragons.colors)
    mydragon['age']=random.randrange(99)
    mydragon['size']=random.randrange(200,399)
    mydragon['breed']=random.choice(helpers.dragons.breeds)
    dragonList.append(mydragon)
print(dragonList)

#ask for user input
while True:
    userinput=input('What do you want to know? ').split()
    if userinput==[]:
        break
    category=userinput[0]
    specification=userinput[1]
    returnList=[]
    m=0
    if category != 'color' and category !='age' and category !='size' and category !='breed':
        print('input error, category not found!')
        continue
    for i in range(len(dragonList)):
        returnList.append(dragonList[i][category])
    for i in returnList:
        if i ==specification:
            m+=1
    if category=='color' or category=='breed':
        print(m,specification,'dragons')
    elif category=='age':
        print(m,specification,'aged','dragons')
    else:
        print(m,specification,'sized','dragons')

#find the largest dragon in each breed
  
for j in helpers.dragons.breeds:
    dragonSize=[]
    for i in range(len(dragonList)):
        if j==dragonList[i]['breed']:
            dragonSize.append(dragonList[i]['size'])
    maximum=max(dragonSize)
    for i in range(len(dragonList)):
        if dragonList[i]['size']==maximum and dragonList[i]['breed']==j:
            info=dragonList[i]
    print('The largest dragon in the breed',j,'is:')
    print(info)
        
    
#dragonbreeder statistics
#average age
dragonAge=[]
m=0
for i in range(len(dragonList)):
    dragonAge.append(dragonList[i]['age'])
for i in range(len(dragonAge)):
    m+=dragonAge[i]
averageAge=m/len(dragonAge)
print('The average age for your dragons is',format(averageAge,'.2f'))

#average size
dragonAvgSize=[]
m=0
for i in range(len(dragonList)):
    dragonAvgSize.append(dragonList[i]['size'])
for i in range(len(dragonAvgSize)):
    m+=dragonAvgSize[i]
averageSize=m/len(dragonAvgSize)
print('The average size for your dragons is',format(averageSize,'.2f'))

#breed distribution
dragonDistribution={}
for j in helpers.dragons.breeds:
    m=0
    for i in range(len(dragonList)):
        if j==dragonList[i]['breed']:
            m+=1
    dragonDistribution[j]=m
sum1=sum(dragonDistribution.values())
for i in dragonDistribution:
    percentage=dragonDistribution[i]/sum1 * 100
    print(i,'accounted for',format(percentage,'.2f'),'percent of your dragon population.')