class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
            return self.head.val
        cnt = 0
        if self.head is None:
            return -1
        curr = self.head
        while cnt != index:
            if curr is None:
                break
            curr = curr.next
            cnt += 1
        if curr is None:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            new_head = ListNode(val)
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            new_tail = ListNode(val)
            self.tail.next = new_tail
            new_tail.prev = self.tail
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        curr = self.head
        cnt = 0

        # Move curr to the node currently at index
        while curr is not None and cnt < index:
            curr = curr.next
            cnt += 1

        # index is greater than the list length
        if cnt < index:
            return

        new_node = ListNode(val)

        # Insert at the head, including an empty list
        if curr == self.head:
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node
            else:
                self.tail = new_node

            self.head = new_node
            return

        # Insert at the tail: index == current length
        if curr is None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

        # Insert before curr
        previous = curr.prev

        previous.next = new_node
        new_node.prev = previous

        new_node.next = curr
        curr.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        curr = self.head
        cnt = 0

        # Find the node at index
        while curr is not None and cnt < index:
            curr = curr.next
            cnt += 1

        # Index is invalid
        if curr is None:
            return

        # Deleting the only node
        if curr == self.head and curr == self.tail:
            self.head = None
            self.tail = None

        # Deleting the head
        elif curr == self.head:
            self.head = curr.next
            self.head.prev = None

        # Deleting the tail
        elif curr == self.tail:
            self.tail = curr.prev
            self.tail.next = None

        # Deleting a middle node
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)