#!/usr/bin/python3
""" Defines a FIFOCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a caching system that uses FIFO algorithm """

    def __init__(self):
        """ Initializes the FIFOCache instance """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the first key inserted into cache_data
                first_key = next(iter(self.cache_data))
                print("DISCARD:", first_key)
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value linked to the given key """
        return self.cache_data.get(key, None)

