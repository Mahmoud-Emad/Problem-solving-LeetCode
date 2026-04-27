from typing import List


class Node:
    def __init__(self, val: int, next: 'Node' = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node = None
    
    def get(self, index: int) -> int:
        if index < 0:
            return -1

        counter = 0
        if index == counter:
            return self.head.val

        head = self.head
        while head != None:
            if counter == index:
                return head.val
            head = head.next
        return -1        

    def insertHead(self, val: int) -> None:
        new_node = Node(val = val)
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val = val)
        if self.head == None:
            self.head = new_node
            return

        head = self.head
        while head.next != None:
            head = head.next

        head.next = new_node

    def remove(self, index: int) -> bool:
        if self.head == None:
            return

        if index == 0:
            self.head = self.head.next

        head = self.head
        counter = 0
        while head is not None and head.next != None:
            if counter == index-1:
                head.next = head.next.next
                return True
            
            head = head.next
            counter += 1
        return False

    def getValues(self) -> List[int]:
        values = []

        head = self.head
        while head != None:
            values.append(head.val)
            head = head.next

        return values
        
