# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:44:12 2022

@author: Admin
"""
array=[]
a = int(input("input a: "))
for i in range(1, a+1):
    if i % 5 == 0:
        array.append(i) #nối phần tử trong mảng
print(array[::-1]) #cú pháp đảo ngược 