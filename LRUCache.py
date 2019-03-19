# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:06:57 2019

@author: BHE
"""
import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.store = collections.OrderedDict()
        self.capacity = capacity
    def get(self, key: int, default = None) -> int:
        """Get an item, return default (None) if not found"""
        if key not in self.store:
            return default
        val = self.store.pop(key)
        self.store[key] = val
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store.pop(key)
        self.store[key] = value
        if len(self.store) > self.capacity:
            self.store.popitem(last = False)
    def clear(self) -> None:
        self.store.clear()
            

