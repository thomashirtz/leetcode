class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k: int):

        def reverseoneGroup(head, k):
            tail = head
            values = []
            for _ in range(k):
                try:
                    values.append(tail.val)
                    tail = tail.next
                except AttributeError:
                    return head, True

            tail = head
            for value in values[::-1]:
                tail.val = value
                tail = tail.next
            return tail, not isinstance(tail, ListNode)

        stop = False
        tail = head
        while not stop:
            tail, stop = reverseoneGroup(tail, k)

        return head
