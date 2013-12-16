# -*- coding:utf-8 -*-
'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

import sys
sys.path.append("../common/")

from daum_openapi.common import *


class contents(object):
    base_url = "http://apis.daum.net/contents/"
    apikey = None
    
    def __init__(self, apikey):
        if apikey is None:
            print "apikey is None."
        else:
            self.apikey = apikey
            
    

    def movie(self, q,  result=10, pageno=1, output='xml'):
        params={}
        params['q'] = q
        params['result'] = result
        params['pageno'] = pageno
        params['output'] = output
        params['apikey'] = self.apikey
         
        return  request(self.base_url+"/movie", params=params)
    

if __name__ == "__main__":
    ct = contents("b3e0456c1bf9facc191106ca35f9871141cb435a")
    print ct.movie("공범", 3, 1, "json")
     