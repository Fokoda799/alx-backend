#!/usr/bin/env python3
"""
FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A catching system that inherits from BaseCaching and
    implements a MRU replacement policy."""

    def __init__(self):
        """constructor calling parent class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key"""
        if key and item:
            if key in self.cache_data:
                # Move the existing item to the end of the dict
                self.cache_data.pop(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the most recently used item
                most_used, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(most_used))
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data
        linked to key"""
        if key in self.cache_data:
            # Move the accessed item to the end of the OrderedDict
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value or None
