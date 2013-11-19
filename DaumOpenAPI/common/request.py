# -*- coding:utf-8 -*-

import requests
import simplejson

'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

def request(url, params):
        r = requests.get(url, params=params)
        print r.url
        if r.status_code == 200:
            return simplejson.loads(r.text)
        else:
            raise Exception(r.text)
