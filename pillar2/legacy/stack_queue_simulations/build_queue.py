"""
🧩 Challenge: Build Queue with `collections.deque`

Simulate a **queue** data structure — like a line of people waiting — using Python’s `collections.deque`.

Write a class `Queue` that supports:
- `enqueue(item)` → adds an element to the *end* of the queue  
- `dequeue()` → removes and returns the *front* element  
- `peek()` → shows the next element to be served (front)  
- `is_empty()` → returns True if the queue has no elements  
- `size()` → returns the number of elements  

Example:
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")
print(q.dequeue())  ➜  "Alice"
print(q.peek())     ➜  "Bob"

Rules:
- Use `collections.deque` instead of a plain list.
- Do not use slicing or indexing for removals.
- Handle underflow (empty queue) safely.
- Remember: **FIFO** → First In, First Out.

Be quick and precise — queues are the backbone of scheduling, ETL job pipelines, and task orchestration systems.
"""
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        if not isinstance(item, int):
            raise TypeError("Queue only accepts integers")
        self.queue.append(item)
    
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def peek(self):
        if not self.queue:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(333)
q.enqueue(4)

print(q.peek())   # ➜ 333
print(q.size())   # ➜ 2
print(q.dequeue())  # ➜ 333
print(q.queue)