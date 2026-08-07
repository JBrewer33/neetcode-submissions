class LRUCache:

    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None
            self.prev = None
            self.val = 0

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.lru:
            curr = self.lru[key]
            self.used(curr)
            return curr.value
        return -1
 
    #adds node to front of linked list
    def used(self, node):
        if node.key in self.lru:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next  = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    #removes lru
    def evict(self):
        toDel = self.tail.prev
        self.tail.prev = toDel.prev
        toDel.prev.next = self.tail
        self.lru.pop(toDel.key)

    def put(self, key: int, value: int) -> None:
        if key not in self.lru:
            newNode = self.Node(key)
            newNode.value = value
            self.used(newNode)
            self.lru[key] = newNode
            
        else:
            self.lru[key].value = value
            self.used(self.lru[key])

        if len(self.lru) > self.cap:
            self.evict()
            
        
