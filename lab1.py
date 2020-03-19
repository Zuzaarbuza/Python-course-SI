# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:58:25 2020

@author: User
"""
numbers = [5,4,3,7,8,10,12,9,2,1,1,1]

def bubblesort(list):

    for i in range(0, len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                t = list[j]
                list[j] = list[j+1]
                list[j+1] = t

list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)


def insertionsort(numbers2):
    for i in range(1, len(numbers2)):
        j = i-1
        next = numbers2[i]
		
        while (numbers2[j] > next) and (j >= 0):
            numbers2[j+1] = numbers2[j]
            j=j-1
        numbers2[j+1] = next

list = [1,4,5,6,8,19,34]
insertionsort(list)
print(list)