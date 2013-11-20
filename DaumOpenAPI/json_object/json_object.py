# -*- coding:utf-8 -*-

import sys, json  
sys.path.append("../search/")

from search import search 
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

class JsonObject(object):
    def __init__( self, result):
        vars(self).update(result)
        
    
    def __repr__(self):
        return str(self.__dict__)  
    
    
     
