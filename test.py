# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:34:55 2019

@author: BHE
"""

import unittest
import LRUCache 

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.cache = LRUCache.LRUCache(2)            
    def test(self):
        self.cache.put(1,400)
        self.cache.put(2,800)
        self.assertEqual(self.cache.get(1), 400)
        self.cache.put(3,1200)
        self.assertEqual(self.cache.get(2), None)
        self.cache.put(4,1600)
        self.assertEqual(self.cache.get(1), None)
        self.assertEqual(self.cache.get(3), 1200)
        self.assertEqual(self.cache.get(4), 1600)
if __name__ == '__main__':
    unittest.main()   