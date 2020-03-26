from doubly_linked_list import DoublyLinkedList


# class LRUCache:
# """
# Our LRUCache class keeps track of the max number of nodes it
# can hold, the current number of nodes it is holding, a doubly-
# linked list that holds the key-value entries in the correct
# order, as well as a storage dict that provides fast access
# to every node stored in the cache.
# """

# def __init__(self, limit=10):
#     # limit
#     self.limit = limit
#     # store key:val
#     self.storage = {}
#     # store order
#     self.dll = DoublyLinkedList()

# """
# Retrieves the value associated with the given key. Also
# needs to move the key-value pair to the end of the order
# such that the pair is considered most-recently used.
# Returns the value associated with the key or None if the
# key-value pair doesn't exist in the cache.
# """

# def get(self, key):
#     for i in self.storage:
#         if i == key:
#             # get value
#             val = self.storage[i]
#             # remove
#             self.storage.pop(i)
#             # set key:val as most recent
#             self.set(i, val)
#             return self.storage[i]
#     return None

# """
# Adds the given key-value pair to the cache. The newly-
# added pair should be considered the most-recently used
# entry in the cache. If the cache is already at max capacity
# before this entry is added, then the oldest entry in the
# cache needs to be removed to make room. Additionally, in the
# case that the key already exists in the cache, we simply
# want to overwrite the old value associated with the key with
# the newly-specified value.
# """

# def set(self, key, value):
#     # if key exists, replace value with current
#     if self.storage.get(key):
#         self.storage[key] = value
#     # if dict at limit
#     elif self.limit == len(self.storage):
#         # enumerate(thing), where thing is either an iterator or a sequence,
#         # returns a iterator that will return (0, thing[0]), (1, thing[1]), (2, thing[2]), and so forth.
#         # https://docs.python.org/2.3/whatsnew/section-enumerate.html
#         for count, item in enumerate(self.storage):
#             # print(f"\n{count}, {item}\n")
#             # least recent at 0
#             if count == 0:
#                 # remove least recent
#                 self.storage.pop(item)
#                 # add new
#                 self.storage[key] = value
#     # if dict not at limit, add
#     else:
#         self.storage[key] = value


# solution from lecture


class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        # self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    def get(self, key):
        # key is not in cache
        if key not in self.storage:
            return None
        # key is in cache
        else:
            # move to most recently used
            node = self.storage[key]
            self.order.move_to_end(node)
            # return value
            return node.value[1]

    def set(self, key, value):
        # scenarios:
        #   size is at limit
        #   size is not at limit
        #   item/key already exists

        # item/key already exists
        if key in self.storage:
            # overwrite value -> where is value stored?
            node = self.storage[key]
            node.value = (key, value)
            # move to tail
            self.order.move_to_end(node)
            return

        # size is at limit
        if len(self.order) == self.limit:
            # remove oldest
            index_of_oldest = self.order.head.value[0]
            del self.storage[index_of_oldest]
            self.order.remove_from_head()
            # add new one to tail

        # size is not at limit
        # add to order
        self.order.add_to_tail((key, value))
        # add to storage
        self.storage[key] = self.order.tail
