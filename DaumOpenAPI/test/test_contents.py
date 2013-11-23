# -*- coding:utf-8 -*-
 
import unittest

import sys
sys.path.append("../contents/")
sys.path.append("../json_object/")

from contents import contents

class TestContentsApiFunctions(unittest.TestCase):

    ct = None
    def setUp(self):
        self.ct = contents("b3e0456c1bf9facc191106ca35f9871141cb435a")

    def test_contents_movie_json(self):
        rc = self.ct.movie(u"공범", 10, 1,"json")
        self.assertEqual(rc.channel.q, u'공범')
        
        
    def test_contents_movie_xml(self):
        rc = self.ct.movie(u"공범", 10, 1,"xml")
        self.assertEqual(rc.channel.q, u'공범')
        
        
    def test_contents_movie_pagecount_zero(self):
        rc = self.ct.movie(u"공범", 10, 0,"xml")
        self.assertEqual(rc.apierror.dcode, u'111')
        

          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestContentsApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)