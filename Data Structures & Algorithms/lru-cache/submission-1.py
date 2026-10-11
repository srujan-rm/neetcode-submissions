class Process:
    def __init__(self, next = None, prev = None, val = None, key = None):
        self.next = next 
        self.prev = prev
        self.val = val
        self.key = key
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.kv = dict() 
        self.old = None 
        self.new = None

    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1 
        if self.kv[key] == self.new:
            return self.new.val
        process = self.kv[key] 
        previous = process.prev
        after = process.next 
        if previous:
            previous.next = after 
        if after:
            after.prev = previous 
        if (self.old == process):
            self.old = process.next
        process.next = None
        process.prev = None
        self.new.next = process 
        process.prev = self.new 
        self.new = process
        return self.new.val 

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.get(key) 
            self.new.val = value 
            return 
        process = Process(None, None, value, key)
        if len(self.kv) < self.capacity:
            self.kv[key] = process
            if not self.new:
                self.old = process
            else:
                self.new.next = process
                process.prev = self.new 
            self.new = process
        else:
            self.kv[key] = process
            self.new.next = process 
            process.prev = self.new 
            self.new = process
            if (self.old.next):
                self.old.next.prev = None 
            new_old = self.old.next
            self.old.next = None
            self.kv.pop(self.old.key)
            del self.old
            self.old = new_old 