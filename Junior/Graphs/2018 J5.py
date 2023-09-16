# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2018 J5 Choose your own path
# Problem Type -> Graph traversal

from collections import deque, defaultdict

def bfs(graph, src):
    queue = deque()
    visited = set()
    queue.append((src, 1))
    visited.add(src)
    while queue:
        curr = queue.popleft()
        if len(graph[curr[0]]) == 0:
            return curr[1]
        for neighbour in graph[curr[0]]:
            if not neighbour in visited:
                visited.add(neighbour)
                queue.append((neighbour, curr[1]+1))

def checkPages(graph, curr, visited = set()):
    if curr in visited: return
    visited.add(curr)
    for neighbour in graph[curr]:
        checkPages(graph, neighbour, visited)
    return len(visited)


graph = dict()
pages = int(input())
for page in range(1, pages+1):
    graph[page] = list(map(int, input().split()[1:]))
print('Y' if checkPages(graph, 1) == pages else 'N')
print(bfs(graph, 1))
