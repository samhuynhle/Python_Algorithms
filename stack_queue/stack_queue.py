# the Python list can be used for implementing a stack
stack = []

# Push items to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# Print the stack
print(stack)

# Remove Items from the stack (will have to remove from the back)
x = stack.pop()

# Stack rule: Last in, first out

from collections import deque
# the deque object is optimizted for adding and removing

queue = deque()

# Add to queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# Remove from queue
x = queue.popleft()

# Queue rule: First in, first out