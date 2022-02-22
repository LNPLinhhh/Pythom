# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 23:02:21 2022

@author: Admin
"""

try:

   a = int(input("Nhập a: "))
   b = int(input("Nhập b: "))  
   if a<80 and 100<b:
       print("khong duoc dau be oi")
   else:       
       for i in range(a, b+1):
           if i % 3 == 0 and i % 2 == 0:
               print(i)
except:
    print("nhap lai di") 