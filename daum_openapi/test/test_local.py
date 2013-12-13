# -*- coding:utf-8 -*-
 
import unittest

import sys
sys.path.append("../local/")
sys.path.append("../json_object/")

from daum_openapi.local import local

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
        {"name3":"삼성2동","code":"1123059","name1":"서울특별시","name2":"강남구"}
        rc = self.lc.coord2addr('37.507502379027','127.05590291409', 'WGS84','simple',"json")
        self.assertEqual(rc.code,u"1123059")
        self.assertEqual(rc.name1,u"서울특별시")
        self.assertEqual(rc.name3,u"삼성2동")
    
    def test_transcoord(self):
        rc = self.lc.transcoord('37.507502379027','127.05590291409', 'WGS84','TM',"json")
        self.assertEqual(rc.__dict__.has_key('x'), True)
        self.assertEqual(rc.__dict__.has_key('y'), True)
        
          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLocalApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)