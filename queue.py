class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        print(self.items)


test_queue = Queue()
test_queue.enqueue("Car")
test_queue.enqueue("Bus")
test_queue.enqueue("Lorry")
test_queue.print_queue()
test_queue.dequeue()
test_queue.print_queue()
