# -*- coding:utf-8 -*-

import requests
import simplejson

def request(url, params):
        r = requests.get(url, params=params)
        print r.url
        if r.status_code == 200:
            return simplejson.loads(r.text)
        else:
            raise Exception(r.text)
         
         
    