#!/usr/bin/env python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A catching system that inherits from BaseCaching and has
    no limits."""

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item
        value for the key key"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data
        linked to key"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
