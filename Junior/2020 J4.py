# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2020 J4 Cyclic Shifts
# Problem Type -> String Algorithms

from collections import deque
t = str(input())
s = str(input())

found = False
def getCyclic(string):
    queue = deque(string)
    cyclic = []
    for _ in range(len(queue)):
        queue.rotate()
        cyclic.append(list(queue))
    return cyclic

len_s = len(s)

if len(t) < len(s):
    found = False
else:
    cyclic = getCyclic(s)
    for i in range(len(t)-len_s+1):
        if list(t[i:len_s+i]) in cyclic:
            found = True
            break
print('yes' if found else 'no')
