class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


test_stack = Stack()
test_stack.push("Bugatti Veyron Sport")
test_stack.push("Bugatti Chiron")
test_stack.pop()

test_stack.print_stack()