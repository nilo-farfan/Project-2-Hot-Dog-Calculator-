# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:19:48 2022

@author: Nilo Farfan
"""

#Project 2 for Intro to Python Class 
#Hot dog calculator 

import math

num_people = int (input ("Enter the number of attendees:" )) 
num_hot_dogs_person = int (input("Enter the number of hot dogs each person will eat:" ))

hd_package = 10 #number of hot dogs each package has
bun_package = 8 #number of buns each package has

a = num_people * num_hot_dogs_person  #total numbers of hot dogs and buns each person will eat

b = a / hd_package 

c = math.ceil(b)

print("\nThe minimum number of packages of hot dogs required:" , c)

d = a/ bun_package

e = math.ceil(d)

print("\nThe minimum number of packages of buns required:" , e)

f = (c*10) - a

print ("\nThe number of hot dogs that will be left over:", f)

g = (e*8) - a

print ("\nThe number of hot dog buns that will be left over:", g)