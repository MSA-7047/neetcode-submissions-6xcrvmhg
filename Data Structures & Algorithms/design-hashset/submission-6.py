class MyHashSet:

    def __init__(self):
        self.hashset = [ListNode(0) for i in range(1000)]        

    def add(self, key: int) -> None:
        current = self.hashset[key % 1000]
        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.hashset[key % 1000]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.hashset[key % 1000]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False
        
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)