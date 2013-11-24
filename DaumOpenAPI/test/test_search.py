# -*- coding:utf-8 -*-

import random
import unittest

import sys
sys.path.append("../search/")
sys.path.append("../result/")

from search import search

class TestSearchApiFunctions(unittest.TestCase):

    sc = None
    def setUp(self):
        self.sc= search("97a3f99c0d5a6b2fdd60e915668366f63939e1b6")

    #blog
    def test_blog_json(self):
        rc = self.sc.blog(q=u"아이유", result=10, pageno=1, sort='date', output='json')
        self.assertEqual(int(rc.channel.result), 10)
        
    def test_blog_xml(self):
        rc = self.sc.blog(q=u"아이유", result=10, pageno=1, sort='date', output='xml')
        self.assertEqual(int(rc.channel.result), 10)

    def test_blog_accu_json(self):
        rc = self.sc.blog(q=u"아이유", result=10, pageno=1, sort='accu', output='json')
        self.assertEqual(int(rc.channel.result), 10)
    
    #web
    def test_web_json(self):
        rc = self.sc.web(q=u"아이유", result=10, pageno=1, output='json')
        self.assertEqual(int(rc.channel.result), 10)
        
    def test_web_xml(self):
        rc = self.sc.web(q=u"아이유", result=10, pageno=1, output='xml')
        self.assertEqual(int(rc.channel.result), 10)
        
    #image
    def test_image_accu_json_xml(self):
        rc_json = self.sc.image(q='아이유', result=10, pageno=1, sort='accu', output='json')
        rc_xml = self.sc.image(q='아이유', result=10, pageno=1, sort='accu', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
    
    def test_image_date_json_xml(self):
        rc_json = self.sc.image(q='아이유', result=10, pageno=1, sort='date', output='json')
        rc_xml = self.sc.image(q='아이유', result=10, pageno=1, sort='date', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
        
    #knowledge
    def test_knowledge_date_all_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date', range='all', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date',range='all', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_knowledge_accu_all_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu', range='all', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu',range='all', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
    
    def test_knowledge_view_all_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view', range='all', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view',range='all', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    
    
    def test_knowledge_date_complete_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date', range='complete', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date',range='complete', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_knowledge_accu_complete_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu', range='complete', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu',range='complete', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_knowledge_view_complete_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view', range='complete', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view',range='complete', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    
    def test_knowledge_date_progress_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date', range='progress', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='date',range='progress', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_knowledge_accu_progress_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu', range='progress', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='accu',range='progress', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_knowledge_view_progress_json_xml(self):
        rc_json = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view', range='progress', output='json')
        rc_xml = self.sc.knowledge(q='naver', result=10, pageno=1, sort='view',range='progress', output='xml')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link) 
    
    #book
    def test_book_meta_popular_all_json_xml(self):
        rc_json = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='popular', output='json', searchType='all')
        rc_xml = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='popular', output='json', searchType='all')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link) 
   
    def test_book_meta_accu_all_json_xml(self):
        rc_json = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='accu', output='json', searchType='all')
        rc_xml = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='accu', output='json', searchType='all')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)
        
    def test_book_meta_date_all_json_xml(self):
        rc_json = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='date', output='json', searchType='all')
        rc_xml = self.sc.book(q='naver', target="meta",cate_id=1, result=10, pageno=1, sort='date', output='json', searchType='all')
        self.assertEqual(rc_json.channel.item[0].link, rc_xml.channel.item[0].link)  
     
     
     
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSearchApiFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)