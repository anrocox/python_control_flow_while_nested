#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

How to define nested while loops in Python?

¿Cómo definir ciclos while anidados en Python?
'''

#create a integer
n = 1

#iterates whilst the value of n is less than or equal to 2
while n <= 2:

    #create a integer
    m = 1

    #iterates whilst the value of m is less than or equal to 2
    while m <= 3:
        print('outer loop iteration {}, nested loop iteration {}'.format(n, m))

        #adds 1 to value m
        m += 1

    #adds 1 to value n
    n += 1
