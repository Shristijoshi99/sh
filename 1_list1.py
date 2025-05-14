# 1. list1.py - List Operations Module

def append1(x):
    lst = []
    lst.append(x)
    return lst

def extend1(l):
    lst = []
    lst.extend(l)
    return lst

def pop():
    lst = [1, 2, 3]
    lst.pop()
    return lst

def remove1(x):
    lst = [1, 2, 3, x]
    lst.remove(x)
    return lst