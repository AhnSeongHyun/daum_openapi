# -*- coding:utf-8 -*-

'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

import sys
sys.path.append("../common/")

from daum_openapi.common import *

class local(object):
    
    base_url = "http://apis.daum.net/local/geo"
    apikey = None
    
    def __init__(self, apikey):
        if apikey is None:
            print "apikey is None."
        else:
            self.apikey = apikey
            
    
    def addr2coord(self, q, pageno, output='xml'): 
        
        params={}
        params['q'] = q
        params['pageno'] = pageno
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/addr2coord", params=params)
        
         
    def coord2addr(self, latitude='', longitude='', inputCoordSystem='WGS84', format='fullname',output='xml'):
        params={}
        params['latitude'] = latitude
        params['longitude'] = longitude
        params['inputCoordSystem'] = inputCoordSystem
        params['format'] = format
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/coord2addr", params=params)
         
    
    def transcoord(self, y='',x='', fromCoord='',toCoord='', output='xml'):
        params={}
        params['x'] = x
        params['y'] = y
        params['fromCoord'] = fromCoord
        params['toCoord'] = toCoord
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/transcoord", params=params)

    
if __name__ == "__main__":
    lc = local("48408559bb754dd16c517a5fd6d01e376a4be151")
    print lc.addr2coord(u"대학로", 1,"json")
    print lc.coord2addr('37.507502379027','127.05590291409', 'WGS84','simple',"json")
    print lc.transcoord('37.507502379027','127.05590291409', 'WGS84','TM',"json")
    
        
     
    
        