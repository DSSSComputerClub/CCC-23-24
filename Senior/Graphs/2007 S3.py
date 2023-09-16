# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2007 S3 Friends
# Problem Type -> Graph Theory

from collections import defaultdict

def checkCycle(graph, pairs):
    for u, v in pairs:
        result = dfs(u, v, graph)
        if result is not None:
            print(f'Yes {result[v]-1}')
        else:
            print('No')

def dfs(curr, target, graph):
    visited = set()
    distance = dict()
    distance[curr] = 0
    stack = []
    stack.append(curr)
    while stack:
        vertex = stack.pop()
        if vertex in visited and target in visited:
            return distance
        if vertex in visited:
            continue
        visited.add(vertex)
        # adds their neighbour to the stack
        neighbour = graph[vertex]
        stack.append(neighbour)
        distance[neighbour] = distance[vertex]+1

    return None



graph = dict()
pairs = []
n = int(input())
for _ in range(n):
    u,v = list(map(int, input().split()))
    graph[u] = v
while True:
    u,v = list(map(int, input().split()))
    if (u,v) == (0,0):
        break
    pairs.append((u,v))

checkCycle(graph, pairs)
