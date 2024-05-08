#!/usr/bin/python3
""" Defines a MRUCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system that uses MRU algorithm """

    def __init__(self):
        """ Initializes the MRUCache instance """
        super().__init__()

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the most recently used key
                mru_key = max(self.cache_data, key=lambda k: self.cache_data[k])
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value linked to the given key """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
