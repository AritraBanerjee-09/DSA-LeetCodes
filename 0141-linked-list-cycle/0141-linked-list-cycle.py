# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # temp = head
        # net_Set = set()

        # while temp is not None:
        #     if temp in net_Set:
        #         return True
        #     net_Set.add(temp)
        #     temp= temp.next
        # return False
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False