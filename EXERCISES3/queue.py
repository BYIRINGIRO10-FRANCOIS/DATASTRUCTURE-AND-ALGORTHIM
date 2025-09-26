from collections import deque
class Queue:
    def __init__(self):
        # Initialize an empty deque to represent the queue
        self.items = deque()

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the front item from the queue (FIFO)
        return self.items.popleft() if self.items else None

    def next(self):
        # Peek at the next item to be served
        return self.items[0] if self.items else None

    def remaining(self):
        # Return a list of all remaining items in the queue
        return list(self.items)

# ----------- QUEUE USAGE EXAMPLES -----------

# Airtel service center example: simulate 5 customers and serve 3
queue = Queue()
for customer in ["Customer1", "Customer2", "Customer3", "Customer4", "Customer5"]:
    queue.enqueue(customer)
for _ in range(3):
    queue.dequeue()  # Serve first 3 customers
print("Next customer:", queue.next())  # Should print "Customer4"

# RRA office example: simulate 4 citizens and serve 2
queue2 = Queue()
for citizen in ["Citizen1", "Citizen2", "Citizen3", "Citizen4"]:
    queue2.enqueue(citizen)
for _ in range(2):
    queue2.dequeue()  # Serve first 2 citizens
print("Remaining citizens:", queue2.remaining())  # Should print ['Citizen3', 'Citizen4']
