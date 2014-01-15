# -*- coding:utf-8 -*-
 
import unittest

import sys
sys.path.append("../contents/")
sys.path.append("../json_object/")

from daum_openapi.contents import contents

class TestContentsApiFunctions(unittest.TestCase):

    ct = None
    def setUp(self):
        self.ct = contents("b3e0456c1bf9facc191106ca35f9871141cb435a")
        print "setup"
        
    def test_contents_movie_pagecount_zero(self):
        rc = self.ct.movie(u"love", 10, 0,"xml") 
        self.assertEqual(rc.apierror.dcode, u'111')
        

          
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestContentsApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)