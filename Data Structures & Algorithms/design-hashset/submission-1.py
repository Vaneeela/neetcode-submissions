class MyHashSet:

    def __init__(self):
        self.items = set()
        

    def add(self, key: int) -> None:
        s = self.items
        if key in s:
            pass
        s.add(key)
        
        

    def remove(self, key: int) -> None:
        s = self.items
        if key in s:
            s.remove(key)
        pass
        

    def contains(self, key: int) -> bool:
        s = self.items
        if key in s:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)