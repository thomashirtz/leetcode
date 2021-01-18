class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        elif not head.next:
            return head
        node = head
        while node.next != None:
            node.val,node.next.val = node.next.val,node.val
            if node.next.next != None:
                node = node.next.next
            else:
                break
        return head