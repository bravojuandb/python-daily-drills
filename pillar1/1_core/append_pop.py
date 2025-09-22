"""
You're managing a queue of customers in a store.

1. Start with an empty list called `queue`.
2. Append the following customer IDs in order: 101, 102, 103.
3. Pop the first customer (simulate serving them).
4. Append two more customers: 104, 105.
5. Pop the last customer (simulate someone leaving suddenly).
6. Return the final state of the queue.

⚡ Be quick — no printing step by step, just write the code and return the list.
"""

# First solution using .append()

queue = []

queue.append(101)
queue.append(102)
queue.append(103)

queue.pop(0)

queue.append(104)
queue.append(105)

queue.pop(-1)

print(queue)


# Second solution using .extend()


queue = []
queue.extend([101, 102, 103])

queue.pop(0)
queue.extend([104, 105])
queue.pop()

print(queue)