# Author: Deon Jerom
# Date: Sept. 2023
# Solution to Single Source Shortest Path
# Problem Type -> Graph Theory

from heapq import heappop, heappush

def dijkstra(graph, start):
    distance = [[float('inf'), None] for vertex in graph]
    distance[start-1][0] = 0
    distance[start-1][1] = start
    pq = [(0,start)]
    visited = set()
    while pq:
        curr_weight, vertex= heappop(pq)
        visited.add(vertex)
        for neighbour, weight in graph[vertex-1]:
            if neighbour not in visited:
                heappush(pq, (weight + curr_weight, neighbour))
                if (curr_weight+weight) < distance[neighbour-1][0]:
                    distance[neighbour-1][0] = (curr_weight+weight)
                    distance[neighbour-1][1] = vertex

    return distance

vertices, edges = list(map(int, input().split()))
graph = [[] for _ in range(vertices)]

for _ in range(edges):
    u,v,w = list(map(int, input().split()))
    graph[u-1].append((v,w))
    graph[v-1].append((u,w))

l = dijkstra(graph, 1)
for vertex in range(1, vertices+1):
    distance = l[vertex-1][0]
    if distance == float('inf'):
        print(-1)
    else:
        print(distance)
