#!/usr/bin/env python3
"""
LFUCache that inherits from BaseCaching and is a caching system
"""
from collections import OrderedDict, defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system that inherits from BaseCaching and
    implements LFU (Least Frequently Used) algorithm."""

    def __init__(self):
        """Constructor that calls the parent class constructor and
        initializes additional data structures."""
        super().__init__()
        self.cache_data = OrderedDict()  # Stores key-value pairs
        self.item_freq = defaultdict(int)  # Stores frequency

    def put(self, key, item):
        """Assigns the item value to the key in self.cache_data."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key already exists, update the item value and
            # increase the frequency
            self.cache_data[key] = item
            self.item_freq[key] += 1
            self.update_cache_order(key)
        else:
            # If the cache is full, discard the lfu item(s)
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.discard_least_frequent()

            # Add the new item to the cache and set its freq to 1
            self.cache_data[key] = item
            self.item_freq[key] = 1

    def get(self, key):
        """Returns the value associated with the key from self
        cache_data."""
        if key is None or key not in self.cache_data:
            return None

        # Increase the frequency of the accessed item and update
        # the cache order
        self.item_freq[key] += 1
        self.update_cache_order(key)

        return self.cache_data[key]

    def update_cache_order(self, key):
        """Updates the cache order by moving the item with the
        given key to the end of the OrderedDict."""
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

    def discard_least_frequent(self):
        """Discards the least frequently used item(s) in the cache
        using LFU and LRU tiebreaker."""
        min_freq = min(self.item_freq.values())
        least_freq_items = [
            k for k, v in self.item_freq.items() if v == min_freq]

        # If there is > than one least freq item, use LRU tiebreaker
        lru_item = next(iter(self.cache_data))
        for key in self.cache_data:
            if key in least_freq_items:
                lru_item = key
                break

        # Discard the LFU item with LRU tiebreaker
        del self.item_freq[lru_item]
        del self.cache_data[lru_item]
        print("DISCARD: {}".format(lru_item))
