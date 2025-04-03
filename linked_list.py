class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Посилання на наступний елемент

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head  # Кільцевий зв'язок
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Оновлення кільцевого зв’язку
        self.size += 1

    def length(self):
        return self.size

    def display(self):
        if not self.head:
            return
        current = self.head
        for _ in range(self.size):
            print(current.value, end=" -> ")
            current = current.next
        print("(повторення першого елемента)")
