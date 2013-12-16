# -*- coding:utf-8 -*-
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''
import sys
sys.path.append("../common/")

from daum_openapi.common import *

class search(object):
    
    base_url = "http://apis.daum.net/search"
    apikey = None
    
    def __init__(self, apikey):
        if apikey is None:
            print "apikey is None."
        else:
            self.apikey = apikey
            
    
    def blog(self, q=None,  result=10, pageno=1, sort='date', output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/blog", params=params)
    
    def web(self, q=None,  result=10, pageno=1, output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/web", params=params)
    
    def board(self, q=None,  result=10, pageno=1, sort='accu', output='json'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno    ']= pageno
        params['sort'] = sort
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/board", params=params)
    
    
    def image(self, q=None,  result=10, pageno=1, sort='accu', output='json'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/image", params=params)
    
    
    def cafe(self, q=None,  result=10, pageno=1, sort='date', output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/cafe", params=params)
    
    def vclip(self, q=None,  result=10, pageno=1, sort='accuracy', output='json'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/vclip", params=params)
    
    def knowledge(self, q=None,  result=10, pageno=1, sort='accuracy', range='all', output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['range'] = range
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/knowledge", params=params)
    
    
    def book(self, q=None,  target='meta', cate_id=None, result=10, pageno=1, sort='popular', searchType='all', output='xml'):
        params={}
        params['q'] = q
        
        params['target'] = target
        
        if cate_id is not None:
            params['cate_id'] = cate_id;
             
        params['result'] = result
        params['pageno']= pageno
        params['sort'] = sort
        params['range'] = range
        params['searchType'] = searchType
        params['output'] = output
        params['apikey'] = self.apikey
        return  request(self.base_url+"/book", params=params)
    


    
     