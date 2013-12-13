# -*- coding:utf-8 -*-

'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

import sys
sys.path.append("../json_object/")

import requests
import json, xmltodict 
from daum_openapi.json_object import *
 
def request(url, params):

        r = requests.get(url, params=params)
        #print r.url
        if r.status_code == 200:
            jsonStr = ""
            
            if params['output'].upper() != 'JSON':
                convertedJson = xmltodict.parse(r.text)
                jsonStr = json.dumps(convertedJson) 
                
            else:
                jsonStr = r.text
                 
            json_obj = json.loads(jsonStr, object_hook= JsonObject)
            return json_obj
        else:
            raise Exception(r.text)
