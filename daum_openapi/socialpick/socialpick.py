# -*- coding:utf-8 -*-
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

import sys
sys.path.append("../common/")

from daum_openapi.common import *
 
class socialpick(object):
    
    base_url = "http://apis.daum.net/socialpick"
    apikey = None
    
    def __init__(self, apikey):
        if apikey is None:
            print "apikey is None."
        else:
            self.apikey = apikey
            
    
    def search(self, n,  category=None, output='xml'):
        params={}
        params['n'] = n
        
        if category is not None:
            params['category'] = category
            
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/search", params=params)
    

if __name__ == "__main__":
    sp = socialpick("a4c8c716d0d6c2d652cede75a6c688dba9d0164c")
    print sp.search(10, "c", "json")
    print sp.search(n=10, output="json")
     
   
        