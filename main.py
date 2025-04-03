from array_list import ArrayBasedList

if __name__ == "__main__":
    my_list = ArrayBasedList()

    my_list.append('A')
    my_list.append('B')
    my_list.append('C')

    my_list.display()
    print("Довжина списку:", my_list.length())

