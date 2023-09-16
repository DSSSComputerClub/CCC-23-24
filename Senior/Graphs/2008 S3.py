# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2008 S3 Maze
# Problem Type -> Graph Theory

from collections import deque

def bfs(start_x, start_y, end_x, end_y, graph):
    if graph[end_y][end_x] == '*':
        return -1
    queue = deque()
    queue.append((start_x, start_y, 1))
    visited = set()
    while queue:
        x,y,distance = queue.popleft()
        if (x,y) == (end_x, end_y):
            return distance;
        if x < 0 or x >= len(graph[0]) or y < 0 or y >= len(graph):
            continue
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if graph[y][x] == '-':
            queue.append((x-1, y, distance+1))
            queue.append((x+1, y, distance+1))
        elif graph[y][x] == '|':
            queue.append((x, y-1, distance+1))
            queue.append((x, y+1, distance+1))
        elif graph[y][x] == '+':
            queue.append((x-1, y, distance+1))
            queue.append((x+1, y, distance+1))
            queue.append((x, y-1, distance+1))
            queue.append((x, y+1, distance+1))

    return -1

paths = []
for _ in range(int(input())):
    graph = []
    r,c = int(input()), int(input())
    for i in range(r):
        graph.append(list(map(str, input())))
    paths.append(bfs(0,0, c-1, r-1, graph))

for path in paths:
    print(path)
