# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:41:44 2018

@author: Win10
"""


def first_function(number):
    if number > 0 :
        return number
    if number < 0 :
        return number*-1 



def second_function(maxvalue):   # funktioniert nur bei kurzen listen
    list.sort()
    return [-1]
    
def second_alternative_function(maxvalue):  # auch für lange listen
    a = maxvalue[0]
    for number in maxvalue:
        if number > a:
            a = number
        else:
            continue
    return a
second_alternative_function       #wenn du die function benutzt musst du das vorher ankündigen
           