#!/usr/bin/python
"""
Take a number from command prompt and terminate the programme once get 42

"""
def number(n=0):
    n = int(raw_input())
    while n != 42:
        n = int(raw_input())
    print n
    return
number(10)
