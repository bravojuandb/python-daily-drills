"""
🧩 Challenge: Build Stack with `list`

Simulate a **stack** data structure using a plain Python list.

Write a class `Stack` that supports:
- `push(item)` → adds an element to the top  
- `pop()` → removes and returns the top element  
- `peek()` → returns the top element *without removing it*  
- `is_empty()` → returns True if the stack is empty  
- `size()` → returns the number of elements

Example:
s = Stack()
s.push(10)
s.push(20)
print(s.peek())   ➜  20
print(s.pop())    ➜  20
print(s.size())   ➜  1

Rules:
- Use only `list` operations (`.append()` and `.pop()`).
- Do *not* use `collections.deque`.
- Do *not* use slicing or reversed().
- Handle underflow (popping from empty stack) gracefully.

Be quick and precise — this pattern underlies recursive calls, expression evaluators, and undo/redo logic.
"""
# A class is a blueprint that groups data (attributes) and behaviors (methods).
# Methods are functions inside the class, belonging to its instances.
# An object is an instance created from a class.

class Stack:  
    """
    Represents a stack data structure using a Python list.
    Provides standard stack operations: push, pop, peek, is_empty, and size.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        
        Creates an internal list to store stack elements.
        """
        self.items = []

    def push(self, item):
        """
        Adds an element to the top of the stack.
        
        Args:
            item: The element to be added.
        
        Returns:
            None
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top element of the stack.
        
        Returns:
            The top element if the stack is not empty; otherwise, None.
        """
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        """
        Returns the top element without removing it from the stack.
        
        Returns:
            The top element if the stack is not empty; otherwise, None.
        """
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        """
        Checks whether the stack is empty.
        
        Returns:
            True if the stack has no elements; False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of elements in the stack.
        
        Returns:
            The count of elements in the stack as an integer.
        """
        return len(self.items)

s = Stack() # Instantiate the class: create an object 's' that follows the blueprint
s.push(10) # Apply the method push() to the instance 's'
s.push(20)
print(s.items)

# Demonstration prints
print("Peek:", s.peek())
print("Is empty:", s.is_empty())
print("Size:", s.size())