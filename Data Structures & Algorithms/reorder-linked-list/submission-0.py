class Solution:
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return

        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        half = n // 2

        stack = []
        node = head
        for _ in range(half):
            stack.append(node)
            node = node.next

        top = None

        if n % 2 == 1:
            top = node
            node = node.next
            top.next = None

        while node:
            temp = node.next
            node.next = top
            top = stack.pop()
            top.next = node
            node = temp
