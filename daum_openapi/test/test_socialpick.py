# -*- coding:utf-8 -*-

import random
import unittest

import sys
sys.path.append("../socialpick/")
sys.path.append("../result/")

from daum_openapi.socialpick import socialpick

class TestSocialPickFunctions(unittest.TestCase):

    sp = None
    def setUp(self):
        self.sp = socialpick("a4c8c716d0d6c2d652cede75a6c688dba9d0164c")

    def test_category_c(self):
        rc = self.sp.search(5,'c', 'json')
        if vars(rc).has_key('message'):
            pass
        else:
            count = len(rc.socialpick.item)
            
            for i in range(0, count):
                 self.assertEqual(int(rc.socialpick.item[i].rank), i+1);
    
    def test_category_s(self):
        rc = self.sp.search(5,'s', 'json')
        if vars(rc).has_key('message'):
            pass
        else:
            count = len(rc.socialpick.item)
            
            for i in range(0, count):
                 self.assertEqual(int(rc.socialpick.item[i].rank), i+1);
    
    def test_category_e(self):
        rc = self.sp.search(5,'e', 'json')
        if vars(rc).has_key('message'):
            pass
        else:
            count = len(rc.socialpick.item)
            
            for i in range(0, count):
                 self.assertEqual(int(rc.socialpick.item[i].rank), i+1);
        
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSocialPickApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)