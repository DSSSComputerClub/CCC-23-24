# Author: Deon Jerom
# Solution to 23 J5 Word Hunt
# Problem Type -> Backtracking/Graph traversal

def dfs(k, word, grid, x, y, dx, dy, turned=False):
    global ans
    if x < 0 or x>= len(grid) or y < 0 or y >= len(grid[x]):
        return
    if grid[x][y] != word[k]:
        return
    if k == len(word)-1:
        ans+=1
        return
    dfs(k+1, word, grid, x + dx, y + dy, dx, dy, turned)
    if not turned and  k >= 1:
        dfs(k+1, word, grid, x - dy, y + dx, -dy, dx, True);
        dfs(k+1, word, grid, x + dy, y - dx, dy, -dx, True);



directions = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1), (1,1)]
grid = []
ans = 0

word = str(input())
row = int(input())
col = int(input())

for _ in range(row):
    grid.append(list(map(str, input().split())))

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == word[0]:
            for dy, dx in directions:
                dfs(0, word, grid, x, y, dx, dy)

print(ans)
