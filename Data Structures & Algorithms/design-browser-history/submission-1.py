class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = Node(homepage)
        self.size = 1
        self.current = self.page
        

    def visit(self, url: str) -> None:
        newPage = Node(url)
        cur = self.current
        cur.next = newPage
        newPage.prev = cur
        cur = cur.next
        self.current = cur
        self.size += 1
        

    def back(self, steps: int) -> str:
        cur = self.current
        f = self.page
        x = []
        for _ in range(steps):
            if cur.prev:
                cur = cur.prev
            else:
                return cur.site
        self.current = cur
        return self.current.site

    def forward(self, steps: int) -> str:
        cur = self.current
        f = self.page
        x = []
        for _ in range(steps):
            if cur.next:
                cur = cur.next
            else:
                return cur.site
        self.current = cur
        return self.current.site
        

class Node:
    def __init__(self, url):
        self.site = url
        self.next = None
        self.prev = None

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)