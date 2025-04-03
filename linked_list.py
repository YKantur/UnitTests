class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def length(self):
        return self.size

    def append(self, element):
        new_node = Node(element)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, element, index):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        new_node = Node(element)
        if index == 0:
            if not self.tail:
                self.tail = new_node
                self.tail.next = self.tail
            else:
                new_node.next = self.tail.next
                self.tail.next = new_node
        else:
            prev = self.tail
            for _ in range(index):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
            if index == self.size:
                self.tail = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        prev = self.tail
        for _ in range(index):
            prev = prev.next
        deleted = prev.next
        prev.next = deleted.next
        if deleted == self.tail:
            self.tail = prev
        self.size -= 1
        return deleted.data

    def deleteAll(self, element):
        if not self.tail:
            return
        prev = self.tail
        current = self.tail.next
        while True:
            if current.data == element:
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                self.size -= 1
            else:
                prev = current
            current = current.next
            if current == self.tail.next:
                break

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        current = self.tail.next
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        copy_list = CircularSinglyLinkedList()
        current = self.tail.next
        for _ in range(self.size):
            copy_list.append(current.data)
            current = current.next
        return copy_list

    def reverse(self):
        prev = None
        current = self.tail.next
        first = current
        for _ in range(self.size):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.tail = first
        self.tail.next = prev

    def findFirst(self, element):
        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                return i
            current = current.next
        return -1

    def findLast(self, element):
        index = -1
        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                index = i
            current = current.next
        return index

    def clear(self):
        self.tail = None
        self.size = 0

    def extend(self, elements):
        current = elements.tail.next
        for _ in range(elements.size):
            self.append(current.data)
            current = current.next

    def display(self):
        if not self.tail:
            print("Empty list")
            return
        current = self.tail.next
        for _ in range(self.size):
            print(current.data, end=" -> ")
            current = current.next
        print("(повторення першого елемента)")
