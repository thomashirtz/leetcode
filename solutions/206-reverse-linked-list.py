class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        list_node = None
        while head:
            list_node_tmp = ListNode(head.val)
            list_node_tmp.next = list_node
            list_node = list_node_tmp
            head = head.next
        return list_node
