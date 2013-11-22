# -*- coding:utf-8 -*-

import random
import unittest

import sys
sys.path.append("../local/")
sys.path.append("../json_object/")

from local import local

class TestLocalApiFunctions(unittest.TestCase):

    lc = None
    def setUp(self):
        self.lc = local("48408559bb754dd16c517a5fd6d01e376a4be151")

    def test_addr2coord_json(self):
        rc = self.lc.addr2coord(u"대학로", 1,"json")
        self.assertEqual(int(rc.channel.pageCount), 153);
        
    def test_addr2coord_xml(self):    
        rc = self.lc.addr2coord(u"대학로", 1,"xml")
        self.assertEqual(int(rc.channel.pageCount), 153);
        
    def test_add2coord_pageno_zero(self):
        rc =  self.lc.addr2coord(u"대학로", 0,"json")
        self.assertEqual(rc.channel.apierror.message, 'page_no:[0]:(Belowed minimum value)1');
        
    def test_coord2addr(self):
        print self.lc.coord2addr('37.507502379027','127.05590291409', 'WGS84','simple',"json")
        
    def test_transcoord(self):
        rc = self.lc.transcoord('37.507502379027','127.05590291409', 'WGS84','TM',"json")
        print rc.__dict__.has_key('x')
        
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLocalApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)