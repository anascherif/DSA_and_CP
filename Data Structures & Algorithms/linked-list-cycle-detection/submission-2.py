# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        ft=head
        while ft and ft.next:
            sl=sl.next
            ft=ft.next.next
            if sl==ft:
                return True
        return False