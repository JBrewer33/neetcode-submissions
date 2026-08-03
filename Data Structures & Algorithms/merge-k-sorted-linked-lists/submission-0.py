# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #push all vals into array, heapify, pop each and build new list
        vals = []
        for l in lists:
            curr = l
            while curr != None:
                vals.append(curr.val)
                curr = curr.next
        
        heapq.heapify(vals)
        ret = None
        curr = None
        while vals:
            val = heapq.heappop(vals)
            node = ListNode(val)
            if ret == None:
                ret = node
            if curr != None:
                curr.next = node
            curr = node
        
        return ret