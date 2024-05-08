#!/usr/bin/python3
""" Defines a LIFOCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a caching system that uses LIFO algorithm """

    def __init__(self):
        """ Initializes the LIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the last key inserted into cache_data
                last_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_key)
                del self.cache_data[last_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value linked to the given key """
        return self.cache_data.get(key, None)

