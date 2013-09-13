#! /usr/bin/env python

###use list as stacks

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print stack.pop()

print stack


####queues

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print queue.popleft()
print queue.popleft()

print queue