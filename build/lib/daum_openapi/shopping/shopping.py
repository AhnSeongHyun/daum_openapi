# -*- coding:utf-8 -*-
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''
import sys
sys.path.append("../common/")

from daum_openapi.common import *


class shopping(object):
    
    base_url = "http://apis.daum.net/shopping/"
    apikey = None
    
    def __init__(self, apikey):
        if apikey is None:
            print "apikey is None."
        else:
            self.apikey = apikey
    
    
    def search(self, q, result=10, pageno=1, sort=None, output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno'] = pageno
        
        if sort is not None:
            params['sort'] = sort
            
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/search", params=params)
        
    
    def detail(self, docid, output='xml'):
        params={}
        params['docid'] = docid    
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/detail", params=params)
        

if __name__ == "__main__":
    sp = shopping("043a78c6b4c1df8335e2fe33917ff5f616eff3f6")
   # print sp.search(u"사과", 3,1,"pop","json")
    print sp.detail(u"K91469436", 'json')
    
        
    
    
    
    
    
    
    
    
    
    