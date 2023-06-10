# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def convertArr(self, head):
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr1=self.convertArr(head)
        arr1.reverse()
        if not arr1:
            return head
        head1 = ListNode(arr1[0])
        current_node = head1
        for val in arr1[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return head1

#https://leetcode.com/problems/reverse-linked-list/submissions/968310600/
#easy