"""
Description:
  - A class to define its structure
  - A class to define its functionality
"""
from builtins import len


class Node:

    def __init__(self, data=None, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr = self.head
        lout = ''
        while itr:
            lout += str(itr.data) + " <=> " if itr.next else str(itr.data)
            itr = itr.next
        print(lout)

    def print_forward(self):
        print("Welcome!")
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -> '
            itr = itr.next
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        last_node = self.get_last_node()
        itr = last_node
        lout = ''
        while itr:
            lout += str(itr.data) + '->' if itr.prev else str(itr.data)
            itr = itr.prev
        print(lout)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begin(self, data):
        node = Node(data, None, None)
        self.head = node

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begin(data)
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr, itr.next)
                if itr.next:
                    itr.next.next.prev = node
                itr.next = node
                break
            count += 1
            itr = itr.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, itr, None)
        itr.next = node

    def insert_values(self, values):
        self.head = None
        if len(values) < 1:
            print("Empty values were passed")
            return
        for item in values:
            self.append(item)

    def remove(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.next.prev = itr
            count += 1
            itr = itr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.print_forward()
    ll.print_backward()
