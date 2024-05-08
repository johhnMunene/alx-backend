#!/usr/bin/python3
""" Defines a LRUCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defines a caching system that uses LRU algorithm """

    def __init__(self):
        """ Initializes the LRUCache instance """
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the least recently used key from recently_used list
                lru_key = self.recently_used.pop(0)
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]
            self.cache_data[key] = item
            self.recently_used.append(key)

    def get(self, key):
        """ Retrieves the value linked to the given key """
        if key in self.cache_data:
            self.recently_used.remove(key)
            self.recently_used.append(key)
            return self.cache_data[key]
        return None
