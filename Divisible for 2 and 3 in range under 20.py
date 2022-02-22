# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:57:20 2022

@author: Admin
"""

a = int(input("Nhập số a: "))
if (a>20):
    print("Không được đâu bé ơi")
if (a<20):
    for i in range(1,a+1):
        if((i % 7==0) or (i % 5 ==0)):
            print(i)