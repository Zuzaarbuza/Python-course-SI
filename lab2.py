# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:23:42 2020

@author: User
"""




from functools import reduce
import numpy 
import time  
def unpackTuple(stream): 
    reduce(numpy.append, stream) 
stream = ([0,4,6,7,6,3,4,6,1,2,7] , 5 )   
#stream = ([9,1,1,1,0,0,0,8,10,11,14,2132323,24234524], 2)     
unpackTuple(stream)

def threshold_bubble(lista, prog):
    greater3 = []
    i = 0
    while len(greater3) < 3:
        if lista[i] > prog:
            greater3.append(i)
        i += 1
    
    
    for i in range(0, len(greater3)):
        for j in range(len(greater3)-1):
            if lista[greater3[j]]<lista[greater3[j+1]]:
                t = greater3[j]
                greater3[j] = greater3[j+1]
                greater3[j+1] = t
    return greater3




def threshold_insert(lista,prog):
    greater3 = []
    i = 0
    while len(greater3) < 3:
        if lista[i] > prog:
            greater3.append(i)
        i += 1
    
    
    for i in range(1, len(greater3)):
        j = i-1
        nxt = greater3[i]
        		
        while (lista[greater3[j]] < lista[nxt]) and (j >= 0):
            greater3[j+1] = greater3[j]
            j=j-1
        greater3[j+1] = nxt
        
    return greater3

test_list = []
for it in range(100000):
    test_list.append(it)
print(test_list)

print(threshold_insert(stream[0],stream[1]))

t = time.time()
print(threshold_insert(test_list,90000))
print(time.time()-t)


t = time.time()
print(threshold_bubble(test_list,90000))
print(time.time()-t)