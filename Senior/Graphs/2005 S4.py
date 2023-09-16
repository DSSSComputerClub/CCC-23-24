# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2005 S4 Pyramid Message Scheme
# Problem Type -> Graph Theory

from collections import defaultdict, deque

l = int(input())
for _ in range(l):
    n = int(input())
    messages = [input() for _ in range(n)]
    root = messages[-1]
    graph = defaultdict(set)
    for i in range(n - 1):
        graph[messages[i]].add(messages[i + 1])
        graph[messages[i + 1]].add(messages[i])
    root = messages[-1]
    queue = deque()
    visited = set()
    queue.append((root, 0))
    simul = []
    while queue:
        root, distance = queue.popleft()
        visited.add(root)
        for neighbour in graph[root]:
            if neighbour not in visited:
                queue.append((neighbour, distance + 1))
                if distance + 1 not in simul:
                    simul.append(distance + 1)
    print(((len(set(messages))-1) * 20 ) - sum([20 for _ in range(len(simul))]))
