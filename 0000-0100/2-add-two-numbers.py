class Solution:
    def addTwoNumbers(self, l1, l2):
        self.addNodes(l1, l2)
        return l1

    def addNodes(self, node1, node2, retenue=0):
        somme = node1.val + node2.val + retenue
        node1.val = somme % 10
        retenue = somme // 10
        if node1.next or node2.next or retenue:
            if not node1.next:
                node1.next = ListNode(0)
            if not node2.next:
                node2.next = ListNode(0)
            self.addNodes(node1.next, node2.next, retenue)