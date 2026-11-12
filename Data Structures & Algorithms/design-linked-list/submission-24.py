class MyLinkedList:
# 1,2,3,4
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        cur = self.head
        # while cur:
        #     print(cur.val, "--------")
        #     cur = cur.next
        # print("end")
        if self.head:
            cur = self.head
            i = index
            while cur:
                if i == 0:
                    return cur.val
                else:
                    cur = cur.next
                    i -= 1
        return -1  

    def addAtHead(self, val: int) -> None:
        newNode = self.Node(val)

        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = self.Node(val)
            cur.next.prev = cur
            self.size += 1
        else:
            self.addAtHead(val)
        


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.size :
            self.addAtTail(val)
            return 
        
        cur = self.head
        for _ in range(index):
            cur = cur.next

        prev = cur.prev
        newNode = self.Node(val)
        prev.next = newNode
        newNode.next = cur
        newNode.prev = prev
        cur.prev = newNode
        self.size += 1


        
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = None
        cur = self.head

        i = 0
        if index == 0:
            self.head = self.head.next
            self.head.prev = None



        while cur.next:
            if i == index:
                break
            else:
                cur = cur.next
                i+= 1
        prev = cur.prev
        nxt = cur.next
        if prev:
            prev.next = nxt
        if nxt:
            nxt.prev = prev
        self.size -=1
# 7,5,1,4
        
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
            self.prev = None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)