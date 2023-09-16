# Author: Deon Jerom
# Solution to 2010 J5 Knight Hop
# Problem Type -> Graph traversal/Find the shortest path

import heapq

def bfs(start_x, start_y, end_x, end_y):
    directions = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]
    queue = []
    heapq.heappush(queue, (0, start_x, start_y))
    visited = set()
    visited.add((start_x,start_y))
    found = []
    while queue:
        distance, x, y = heapq.heappop(queue)
        if (x,y) == (end_x,end_y):
            found.append(distance)
        for dx,dy in directions:
            temp_x,temp_y = x+dx,y+dy
            if 0 >= temp_x or temp_x > 8 or 0 >= temp_y or temp_y > 8 or (temp_x,temp_y) in visited:
                continue
            visited.add((temp_x,temp_y))
            heapq.heappush(queue, (distance+1, temp_x,temp_y))
    return min(found)

start_x,start_y = map(int,input().split())
end_x,end_y = map(int,input().split())

print(bfs(start_x,start_y,end_x,end_y))
