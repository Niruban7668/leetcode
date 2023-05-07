class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=[]
        list2=[]
        itr=head
        while(itr!=None):
            list1.append(itr.val)
            itr=itr.next
        for i in range(len(list1)):
            if(list1[i] not in list2):
                list2.append(list1[i])
        if not list2:
            return None
        head1 = ListNode(list2[0])
        current_node = head1
        for val in list2[1:]:
            current_node.next = ListNode(val)
            current_node = current_node.next
        return head1