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
        
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4); 
    
    def test_category_s(self):
        rc = self.sp.search(5,'s', 'json')
        
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4); 
    
    def test_category_e(self):
        rc = self.sp.search(5,'e', 'json')
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4); 
    
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSocialPickApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)