from linked_list import CircularSinglyLinkedList
from array_list import ArrayBasedList

def demo_list(lst):
    print("\nПочатковий список (порожній):")
    print("Довжина:", lst.length())

    print("\nДодаємо елементи A, B, C:")
    lst.append('A')
    lst.append('B')
    lst.append('C')
    print("Довжина:", lst.length())

    print("\n Отримуємо елемент за індексом 1:", lst.get(1))

    print("\n Вставляємо 'X' на позицію 1:")
    lst.insert('X', 1)
    print("Елемент на позиції 1:", lst.get(1))

    print("\nВидаляємо елемент на позиції 2:")
    print("Видалений елемент:", lst.delete(2))
    print("Довжина після видалення:", lst.length())

    print("\nШукаємо перше входження 'A':", lst.findFirst('A'))
    print("Шукаємо останнє входження 'A':", lst.findLast('A'))

    print("\n♻Копіюємо список:")
    copy_list = lst.clone()
    print("Довжина копії:", copy_list.length())

    print("\nПеревертаємо список:")
    lst.reverse()
    print("Елемент на позиції 0 після перевороту:", lst.get(0))

    print("\nДодаємо новий список ['D', 'E', 'F']:")
    another_list = CircularSinglyLinkedList() if isinstance(lst, CircularSinglyLinkedList) else ArrayBasedList()
    another_list.append('D')
    another_list.append('E')
    another_list.append('F')
    lst.extend(another_list)
    print("Довжина після розширення:", lst.length())

    print("\nОчищаємо список")
    lst.clear()
    print("Довжина після очищення:", lst.length())


print("\nТестуємо CircularSinglyLinkedList")
demo_list(CircularSinglyLinkedList())

print("\nТестуємо ArrayBasedList")
demo_list(ArrayBasedList())
