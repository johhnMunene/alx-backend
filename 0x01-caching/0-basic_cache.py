#!/usr/bin/python3
""" Defines a BasicCache class that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defines a basic caching system """

    def put(self, key, item):
        """ Assigns the item value to the key in cache_data """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves the value linked to the given key """
        return self.cache_data.get(key, None)
