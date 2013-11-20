# -*- coding:utf-8 -*-
import sys
sys.path.append("../json_object/")

import requests
import json 
from json_object import *


'''
Created on 2013. 11. 2.
@author: seonghyunan
'''

def request(url, params):
        r = requests.get(url, params=params)
        print r.url
        if r.status_code == 200:
            
            if params['output'].upper() == 'XML':
                pass
            else:
                json_obj = json.loads(r.text, object_hook= JsonObject)
                return json_obj

        else:
            raise Exception(r.text)
