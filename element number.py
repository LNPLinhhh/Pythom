# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:07:13 2022

@author: Admin
"""
a = int(input("input a: "))
b = True
for i in range(1, a/2):
    if a % i != 0:
        b = False
    if a % i == 0:
        b = True
if b == False:
    print(a, "la so nguyen to")
if b == True:
    print(a, "khong la so nguyen to")