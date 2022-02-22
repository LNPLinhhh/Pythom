# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:33:36 2022

@author: Admin
"""

array=[]
a = int(input("Nhap so a: "))
for i in range (1, a+1):
    if(i % 10 == 5):
        array.append(i)
print(array)