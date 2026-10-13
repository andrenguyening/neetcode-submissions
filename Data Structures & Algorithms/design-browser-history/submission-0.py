class ListNode:
    def __init__(self,url,prev=None,next=None):
        self.url = url
        self.prev = prev
        self.next = next
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        self.count = 0

    def visit(self, url: str) -> None:
        new_page = ListNode(url)
        self.curr.next = new_page
        new_page.prev = self.curr
        self.curr = self.curr.next

        self.count += 1


    def back(self, steps: int) -> str:
        while self.curr.prev is not None:
            if steps == 0:
                return self.curr.url
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while self.curr.next is not None:
            if steps == 0:
                return self.curr.url
            steps -= 1
            self.curr = self.curr.next
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)