# -*- coding:utf-8 -*-
 
import unittest

import sys
sys.path.append("../json_object/")

from json_object import *

class TestJsonObjectFunctions(unittest.TestCase):

    testDict = {}
    def setUp(self):
        self.testDict['name'] = u"ash84"
        self.testDict['age'] = 30
        
        like = ['comic','coding','tv'];
        self.testDict['like'] = like
        
        

    def test_jsonobject(self):
        jsonObj = JsonObject(self.testDict)
        self.assertEqual(jsonObj.name,u'ash84')
        self.assertEqual(jsonObj.age,30)
        self.assertEqual(jsonObj.like[0],u'comic')
        self.assertEqual(jsonObj.like[1],u'coding')
        self.assertEqual(jsonObj.like[2],u'tv')
        
        
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonObjectFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)