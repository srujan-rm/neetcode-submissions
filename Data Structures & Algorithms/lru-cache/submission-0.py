class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv = dict()
    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        result = self.kv.pop(key)
        self.kv[key] = result 
        return result
    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.kv.pop(key) 
            self.kv[key] = value
            return
        if (len(self.kv) < self.capacity):
            self.kv[key] = value 
        else:
            self.kv.pop(next(iter(self.kv)))
            self.kv[key] = value 
