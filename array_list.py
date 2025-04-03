class ArrayBasedList:
    def __init__(self):
        self.data = []  # Використовуємо вбудований list

    def append(self, value):
        self.data.append(value)

    def length(self):
        return len(self.data)

    def display(self):
        if not self.data:
            print("Список порожній")
        else:
            print(" -> ".join(self.data))

