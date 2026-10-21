# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return None
        #Find Mid using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow.next
        #Disconnect the nodes in the mid
        slow.next = None
        #Reverse the 2nd half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #Connect Alternate nodes
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            