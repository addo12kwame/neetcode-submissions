# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeTwoLists(self, list1: ListNode, list2:ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = None
        cur = ListNode()
        head = cur
        l= list1
        r = list2
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if l:
            cur.next = l
        if r:
            cur.next = r

        return head.next 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        size = 1
        n = len(lists)
        while size < n:
            for left in range(0,n, 2 * size):
                mid =   left + size
                if mid < n:
                    lists[left] = self.mergeTwoLists(
                    lists[left],
                    lists[mid]
                    )

            size = size * 2
        
        return lists[0] if n > 0 else None