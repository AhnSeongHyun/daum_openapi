# -*- coding:utf-8 -*-

import random
import unittest

import sys
sys.path.append("../socialpick/")
sys.path.append("../result/")

from socialpick import socialpick

class TestSocialPickFunctions(unittest.TestCase):

    sp = None
    def setUp(self):
        self.sp = socialpick("a4c8c716d0d6c2d652cede75a6c688dba9d0164c")

    def test_category_c(self):
        rc = self.sp.search(10,'c', 'json')
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4);
        self.assertEqual(int(rc.socialpick.item[4].rank), 5);
        self.assertEqual(int(rc.socialpick.item[5].rank), 6);
        self.assertEqual(int(rc.socialpick.item[6].rank), 7);
        self.assertEqual(int(rc.socialpick.item[7].rank), 8);
        self.assertEqual(int(rc.socialpick.item[8].rank), 9);
        self.assertEqual(int(rc.socialpick.item[9].rank), 10);
        
    
    def test_category_s(self):
        rc = self.sp.search(10,'s', 'json')
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4);
        self.assertEqual(int(rc.socialpick.item[4].rank), 5);
        self.assertEqual(int(rc.socialpick.item[5].rank), 6);
        self.assertEqual(int(rc.socialpick.item[6].rank), 7);
        self.assertEqual(int(rc.socialpick.item[7].rank), 8);
        self.assertEqual(int(rc.socialpick.item[8].rank), 9);
        self.assertEqual(int(rc.socialpick.item[9].rank), 10);
    
    def test_category_e(self):
        rc = self.sp.search(10,'e', 'json')
        self.assertEqual(int(rc.socialpick.item[0].rank), 1);
        self.assertEqual(int(rc.socialpick.item[1].rank), 2);
        self.assertEqual(int(rc.socialpick.item[2].rank), 3);
        self.assertEqual(int(rc.socialpick.item[3].rank), 4);
        self.assertEqual(int(rc.socialpick.item[4].rank), 5);
        self.assertEqual(int(rc.socialpick.item[5].rank), 6);
        self.assertEqual(int(rc.socialpick.item[6].rank), 7);
        self.assertEqual(int(rc.socialpick.item[7].rank), 8);
        self.assertEqual(int(rc.socialpick.item[8].rank), 9);
        self.assertEqual(int(rc.socialpick.item[9].rank), 10);
    
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSocialPickApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)