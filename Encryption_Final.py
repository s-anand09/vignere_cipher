# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 01:58:50 2021

@author: shrey
"""
from Sb_ch import *
msg=input("Input the message: ")
key=input("Input the key: ")
lkey=len(key)
j=0
for i in range(lkey,len(msg)):
    if j==len(key):
        j=0
    key=key+key[j]
    j=j+1

def encrypt(messagef,keyf,sB,ch):
    final=""
    for i in range(0, len(messagef)):
        x=messagef[i]
        y=keyf[i]
        x1=ch.index(x)
        y1=ch.index(y)
        final=final+sB[y1][x1]
    return final
    
encrypt1=encrypt(msg,key,sBox,chararray)
encrypt2=encrypt(encrypt1,key,sBox,chararray)
encrypt3=encrypt(encrypt2,key,sBox,chararray)
encrypt_final=encrypt(encrypt3,key,sBox,chararray)
    
print(encrypt_final)

