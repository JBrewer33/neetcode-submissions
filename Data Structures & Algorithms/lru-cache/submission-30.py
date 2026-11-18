class Node:

    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key #key cooresponding to node in map


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self. size = 0
        self.nodes = {} #dictionary {key, Node} allows retreval of any node in linked list based on value
        self.lruHead = None
        self.lruTail = None



    def addToFront(self, node):
        #if there is at least one node already in linked list
        if self.lruHead != None:
            #new next
            node.next = self.lruHead
            #new prev
            node.prev = None
            
            #old prev
            node.next.prev = node
            #head
            self.lruHead = node
        else:
            self.lruHead = node
            self.lruTail = node
            node.next = None
            node.prev = None

    def evict(self):
        tail = self.lruTail
        #if tail.prev exists
        if tail.prev != None:
            #new tail
            self.lruTail = tail.prev
            self.lruTail.next = None
        #else
        else:
            #tail, head = none
            self.lruTail = None
            self.lruHead = None
        
        #remove from map
        self.nodes.pop(tail.key)
        #decrement size
        self.size -= 1


    def removeNode(self, node):
        if node.next != None and node.prev != None: #middle of list 
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next != None: #next exists prev doesnt is curr head
            self.lruHead = node.next
            node.next.prev = None
        elif node.prev != None: #prev exists next doesnt is curr tail
            self.lruTail = node.prev
            node.prev.next = None
        else:
            self.lruHead = None
            self.lruTail = None

        node.next = None
        node.prev = None
            

    def get(self, key: int) -> int:
        #if not in map
        if key not in self.nodes:
            return -1
            #return -1
        #else
        else:
            curr = self.nodes[key]
            #remove from lru
            self.removeNode(curr)
            #place at front of lru
            self.addToFront(curr)
            #return value
            return curr.value




    def put(self, key: int, value: int) -> None:
        #if key not in map
        if key not in self.nodes:
            #create new node
            newNode = Node(key, value)
            # add to map
            self.nodes[key] = newNode
            # add to front of lru
            self.addToFront(newNode)
            #increment size
            self.size += 1

            #if lru over capacity
            if self.size > self.capacity:
                #remove tail node from lru
                #remove node from map -- need to be able to get key of tail node
                self.evict()
        #else
        else:
            #take existing node
            curr = self.nodes[key]
            #update value
            curr.value = value
            #remove from lru
            self.removeNode(curr)
            #place at front
            self.addToFront(curr)

            
        
