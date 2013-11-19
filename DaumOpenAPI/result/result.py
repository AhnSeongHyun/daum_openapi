# -*- coding:utf-8 -*-

import sys, json  
sys.path.append("../search/")

from search import search 
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

class result(object):
     
    def __init__(self, output, resultStr):
        if output.upper() == 'XML':
            self.parserXml(resultStr)
        elif output.upper() == 'JSON':
            self.parseJson(resultStr)
        else:
            raise Exception("unknown output")
        
    def parseXml(self, resultStr):
        pass
    
    def parseJson(self, resultStr): 
        pass 
        

         
         
    
if __name__ == "__main__":
    sc = search('97a3f99c0d5a6b2fdd60e915668366f63939e1b6')
    resultStr = sc.blog(u'아이유', 10, 1, 'date', 'json');   
    rc = result('json', resultStr)
    
    
    
     