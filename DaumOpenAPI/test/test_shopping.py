# -*- coding:utf-8 -*-
 
import unittest

import sys
sys.path.append("../shopping/")
sys.path.append("../json_object/")

from shopping import shopping

class TestShoppingApiFunctions(unittest.TestCase):

    sp = None
    def setUp(self):
        self.sp = shopping("043a78c6b4c1df8335e2fe33917ff5f616eff3f6")
 
    def test_shopping_search_json(self):
        rc = self.sp.search(u"노트북", 10, 1,"pop", "json")
        self.assertEqual(int(rc.channel.result), 10)
        
    def test_shopping_search_xml(self):
        rc = self.sp.search(u"노트북", 10, 1,"pop", "xml")
        self.assertEqual(int(rc.channel.result), 10)
        
    def test_shopping_search_rss(self):
        rc = self.sp.search(u"노트북", 10, 1,"pop", "rss")
        self.assertEqual(int(rc.channel.result), 10)
        
        
    def test_shopping_detail(self):
        rc = self.sp.search(u"노트북", 10, 1,"pop", "rss")
        docid = rc.channel.item[0].docid
        rc1 =self.sp.detail(docid, 'xml')
        self.assertEqual(docid, rc1.channel.item.docid)
        

          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShoppingApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)