# -*- coding:utf-8 -*-

import random
import unittest

import sys
sys.path.append("../local/")

from local import local

class TestLocalApiFunctions(unittest.TestCase):

    lc = None
    def setUp(self):
        self.lc = local("48408559bb754dd16c517a5fd6d01e376a4be151")

    def test_addr2coord(self):
        print self.lc.addr2coord(u"대학로", 1,"json")
        
    def test_coord2addr(self):
        print self.lc.coord2addr('37.507502379027','127.05590291409', 'WGS84','simple',"json")
        
    def test_transcoord(self):
        print self.lc.transcoord('37.507502379027','127.05590291409', 'WGS84','TM',"json")
        
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLocalApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)