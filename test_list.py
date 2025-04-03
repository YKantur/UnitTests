import unittest
from array_list import ArrayBasedList
from linked_list import CircularSinglyLinkedList

class TestArrayBasedList(unittest.TestCase):

    def setUp(self):
        self.list = ArrayBasedList()

    def test_append_and_length(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        self.assertEqual(self.list.length(), 3)

    def test_insert(self):
        self.list.append('A')
        self.list.append('C')
        self.list.insert('B', 1)
        self.assertEqual(self.list.get(1), 'B')

    def test_delete(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        self.assertEqual(self.list.delete(1), 'B')
        self.assertEqual(self.list.length(), 2)

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.list.delete(0)

    def test_findFirst(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.assertEqual(self.list.findFirst('A'), 0)

    def test_findLast(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.assertEqual(self.list.findLast('A'), 2)

    def test_clear(self):
        self.list.append('A')
        self.list.append('B')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

class TestCircularSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = CircularSinglyLinkedList()

    def test_append_and_length(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        self.assertEqual(self.list.length(), 3)

    def test_insert(self):
        self.list.append('A')
        self.list.append('C')
        self.list.insert('B', 1)
        self.assertEqual(self.list.get(1), 'B')

    def test_delete(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('C')
        self.assertEqual(self.list.delete(1), 'B')
        self.assertEqual(self.list.length(), 2)

    def test_findFirst(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.assertEqual(self.list.findFirst('A'), 0)

    def test_findLast(self):
        self.list.append('A')
        self.list.append('B')
        self.list.append('A')
        self.assertEqual(self.list.findLast('A'), 2)

    def test_clear(self):
        self.list.append('A')
        self.list.append('B')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_fail_example(self):
        self.assertEqual(1, 2)  # Завжди падає


if __name__ == '__main__':
    unittest.main()
