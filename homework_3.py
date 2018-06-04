# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:21:51 2018

@author: Win10
"""




def average(listy):
    a=len(listy)
    b=sum(listy)
    c = b / a
    print(c)
    
#average([1,3,4,5,1])


def median(list):                           # why are you not working >:(
    import statistics
    print(statistics.median(list))
    
#median([1,3,4,2,1])





















def greed(name):   #wofür str?
    print("Dear ",str(name), ",")     # kann auch danach nochmal weiter schreiben
    print("how is life going? I´m doing good!")
    
#greed("Shiromi")