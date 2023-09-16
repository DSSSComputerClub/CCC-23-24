# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2009 S4 Shop and Ship
# Problem Type -> Graph Theory

import sys
def dijktras(matrix, start, pencil_locations):
    distances = [float('inf') for _ in range(len(matrix))]
    distances[start - 1] = 0
    visited = set()
    while len(visited) < len(matrix):
        # Find minimum distance vertex not yet visited
        current_min = float('inf')
        current_vertex = None
        for vertex in range(len(distances)):
            if vertex not in visited and distances[vertex] < current_min:
                current_min = distances[vertex]
                current_vertex = vertex

        # Mark vertex as visited
        visited.add(current_vertex)

        # Update distances
        for neighbour in range(len(matrix[current_vertex])):
            if matrix[current_vertex][neighbour] > 0:
                new_dist = distances[current_vertex] + matrix[current_vertex][neighbour]
                if new_dist < distances[neighbour]:
                    distances[neighbour] = new_dist

    return findMinimumPath(distances, pencil_locations)
def findMinimumPath(distances, pencil_locations):
    min_cost = float('inf')
    for vertex, cost in pencil_locations:
        min_cost = min(distances[vertex-1] + cost, min_cost)
    return min_cost

input = sys.stdin.readline

cities = int(input())
matrix = [[0 for col in range(cities)] for row in range(cities)]
trade_routes = int(input())

pencils = []
for _ in range(trade_routes):
    y,x,cost = list(map(int, input().split()))
    matrix[y-1][x-1] = cost
    matrix[x-1][y-1] = cost
numb_pencils = int(input())
for _ in range(numb_pencils):
    pencils.append(tuple(map(int, input().split())))

destination = int(input())

print(dijktras(matrix, destination, pencils))
