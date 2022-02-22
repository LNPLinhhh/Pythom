# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 21:48:26 2022

@author: Admin
"""
a = int(input("Nhập số a: "))
if (a>10):
    print("Số nhập vào phải bé hơn hoặc bằng 10.")
if (a<10):
    for i in range (1, a+1):
        print(i)