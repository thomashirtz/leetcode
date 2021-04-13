class Solution:
    def numComponents(self, head, G):
        self.total = 0

        def follow(head, connected=False):
            if head:
                if head.val in G:
                    self.total += [0, 1][connected is False]
                    follow(head.next, True)
                else:
                    follow(head.next, False)

        follow(head)
        return self.total