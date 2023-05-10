class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def convertArr(self, head):
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.val)
            curr = curr.next
        return arr
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        num3 = 0
        arr1 = self.convertArr(l1)
        arr2 = self.convertArr(l2)
        arr3 = []
        arr4 = []
        for i in reversed(arr1):
            num1 = (num1 * 10) + i
        for j in reversed(arr2):
            num2 = (num2 * 10) + j
        num3 = num1 + num2
        arr3 = [int(x) for x in str(num3)]
        arr4 = arr3[::-1]
        head1 = ListNode(arr4[0])
        current_node = head1
        for val in arr4[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return head1

#https://leetcode.com/problems/add-two-numbers/description/
#mediums