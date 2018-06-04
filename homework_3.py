# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:21:51 2018

@author: Win10
"""




def average(listy):
    if type(listy) is list and if listy:  #schauen ob es sich überhaupt um eine liste handelt und ob die liste nicht leer ist
        Anzahl = len(listy)
        Gesamt = sum(listy)
        c = Gesamt / Anzahl
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