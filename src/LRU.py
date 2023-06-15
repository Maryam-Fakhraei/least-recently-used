class LRU:
    # It makes an LRU that has a specific capacity and gives an OK output
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    # Check the key value is present in the LRU or not. If it doesn't have a unit, give us -1.
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]

    # It updates the value inside the LRU.
    # If the chach is full, it will delete the value that was used later and save it as a key-value.
    # It will output null.
    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.queue) == self.capacity:
            del self.cache[self.queue.pop(0)]
        self.queue.append(key)
        self.cache[key] = value