#doubly linked list for cache
#hash map to store pointers for each node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = defaultdict(Node)
        self.capacity = capacity
        self.size = 0
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    #update to front of lru
    def used(self, curr: Node):

        #remove curr from place, update prev pointer for next and next pointer for prev
        curr.prev.next = curr.next 
        curr.next.prev = curr.prev 

        #put at front of list, update head.next, curr.prev, curr.next, head.next.prev, double check order
        curr.prev = self.head 
        curr.next = self.head.next 
        self.head.next.prev = curr
        self.head.next = curr
    
    def evictLru(self):
        curr = self.tail.prev
        self.nodes.pop(curr.key)
        self.tail.prev = curr.prev
        curr.prev.next = self.tail
        self.size -= 1


    #check map for key, if exists update lru list and return else return -1
    def get(self, key: int) -> int:
        if key in self.nodes:
            self.used(self.nodes[key])
            return self.nodes[key].value

        return -1

        
    #if key exists update value, else add key and value, then update lru list oldest if needed
    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            newNode = Node(key, value)
            newNode.prev = self.head
            newNode.next = self.head.next
            self.head.next.prev = newNode
            self.head.next = newNode
            self.nodes[key] = newNode
            self.size += 1
        else:
            self.nodes[key].value = value
            self.used(self.nodes[key])

        

        if self.size > self.capacity:
            self.evictLru()
        
            
