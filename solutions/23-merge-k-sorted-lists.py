from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        head = tail = ListNode(0)
        queue = PriorityQueue()

        for idx, node in enumerate(lists):
            if node:
                queue.put((node.val, idx, node))

        while not queue.empty():
            _, idx, node = queue.get()
            if node.next:
                queue.put((node.next.val, idx, node.next))
            tail.next = ListNode(node.val)
            tail = tail.next

        return head.next