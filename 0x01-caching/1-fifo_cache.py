#!/usr/bin/env python3
"""
FIFOCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A catching system that inherits from BaseCaching and
    implements a FIFO replacement policy."""

    def __init__(self):
        """constructor calling parent class constructor"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key key"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > super().MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]

    def get(self, key):
        """return the value in self.cache_data
        linked to key"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
