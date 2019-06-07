# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:16:33 2019

@author: ssn
"""

subject=int(input("enter the no.of subject:"))
a=[]
b=[]
c=[]
d=[]
e=[]
for i in range(0,subject):
    res=0
    a.append(int(input("enter the no. of marks a:")))
    print(a)
    f=float(sum(a)/len(a))
    print(f)

for i in range(0,subject):
    res=0
    b.append(int(input("enter the no. of marks b:")))
    print(b)
    k=float(sum(b)/len(b))
    print(k)
for i in range(0,subject):
    res=0
    c.append(int(input("enter the no. of marks c:")))
    print(c)
    g=float(sum(c)/len(c))
    print(g)
for i in range(0,subject):
    res=0
    d.append(int(input("enter the no. of marks d:")))
    print(d)
    h=float(sum(d)/len(d))
    print(i)
for i in range(0,subject):
    res=0
    e.append(int(input("enter the no. of marks e:")))
    print(e)
    j=float(sum(e)/len(e))
rank=[f,k,g,h,j]
rank.sort()
print(rank[-2])