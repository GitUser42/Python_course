# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:21:51 2018

@author: Win10
"""


class mathematik:

    def average(liste):
        if type(liste) is list and liste:  #schauen ob es sich überhaupt um eine liste handelt und ob die liste nicht leer ist
            Anzahl = len(liste)
            Gesamt = sum(liste)
            c = Gesamt / Anzahl
            print(c)
    
   

    def median(list):                           # why are you not working >:(
        import statistics
        print(statistics.median(list))



    average([1,3,4,5,1])
    
    median([1,3,4,2,1])



















def greed(name):   #wofür str?
    print("Dear ",str(name), ",")     # kann auch danach nochmal weiter schreiben
    print("how is life going? I´m doing good!")
    
#greed("Shiromi")