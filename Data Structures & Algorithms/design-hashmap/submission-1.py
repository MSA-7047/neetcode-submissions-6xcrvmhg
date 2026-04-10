class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0) for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        current = self.hashmap[key % 1000]
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        current = self.hashmap[key % 1000]
        while current.next:
            if current.next.key == key:
                return current.next.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.hashmap[key % 1000]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
        
        
class ListNode:
    def __init__(self, key, val = None):
        self.key = key
        self.val = val
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)