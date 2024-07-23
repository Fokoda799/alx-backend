#!/usr/bin/env python3
"""
FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A catching system that inherits from BaseCaching and
    implements a LRU replacement policy."""

    def __init__(self):
        """constructor calling parent class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key key"""
        if key and item:
            # Check if the cache is already full
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Discard the most recent item
                last_key = next(reversed(self.cache_data))
                print("DISCARD: {}".format(last_key))
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key)
