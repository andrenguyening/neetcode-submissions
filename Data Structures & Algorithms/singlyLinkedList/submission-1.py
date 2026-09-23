class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cnt = 0
        cur = self.head
        while cur != None:
            if cnt == index:
                return cur.val
            cur = cur.next
            cnt += 1
        return -1

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            if self.tail is None:
                self.tail = self.head
        else:
            new_head = ListNode(val)
            new_head.next = self.head
            self.head = new_head


    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.tail = ListNode(val)
            if self.head is None:
                self.head = self.tail
        else:
            new_tail = ListNode(val)
            self.tail.next = new_tail
            self.tail = new_tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        cnt = 0
        cur = self.head
        while cur != None and cur.next != None:
            if cnt == index - 1:
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
                return True
            cur = cur.next
            cnt += 1
        return False


    def getValues(self) -> List[int]:
        ret = []
        cur = self.head
        while cur != None:
            ret.append(cur.val)
            cur = cur.next
        return ret
        
