# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        # Step1 .Find middle using slow and fast pointer
        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # Slow pointer is guarantedd to land on the middle of the LL
        # Cut the list to half
        second = slow.next
        slow.next = None


        # Step 2. Reversed second half LL
  
        prev = None
        while second :
            temp = second.next
            second.next = prev 
            prev = second
            second = temp
        
        # Handle last node to point to previous node
        second = prev

        # Step 3. Merged first half and reversed second half
        curr = head
        while second:
            temp1 = curr.next
            temp2 = second.next

            curr.next = second
            second.next = temp1

            curr = temp1
            second = temp2
        