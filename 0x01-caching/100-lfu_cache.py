#!/usr/bin/python3
""" Defines a LFUCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Defines a caching system that uses LFU algorithm """

    def __init__(self):
        """ Initializes the LFUCache instance """
        super().__init__()
        self.cache_frequency = {}

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.cache_frequency.values())
                items_to_discard = [k for k, v in self.cache_frequency.items() if v == min_freq]
                if len(items_to_discard) > 1:
                    # If there are multiple items with the least frequency, use LRU to discard
                    lru_key = min(self.cache_data, key=lambda k: self.cache_data[k])
                    print("DISCARD:", lru_key)
                    del self.cache_data[lru_key]
                    del self.cache_frequency[lru_key]
                else:
                    lfu_key = items_to_discard[0]
                    print("DISCARD:", lfu_key)
                    del self.cache_data[lfu_key]
                    del self.cache_frequency[lfu_key]
            self.cache_data[key] = item
            self.cache_frequency[key] = 0

    def get(self, key):
        """ Retrieves the value linked to the given key """
        if key in self.cache_data:
            self.cache_frequency[key] += 1
            return self.cache_data[key]
        return None

