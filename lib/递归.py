#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/10 16:50
# Author     : pan
# @File     : 递归.py
# @Software : PyCharm

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))