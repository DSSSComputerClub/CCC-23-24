# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2023 S1 Trianglane
# Problem Type -> Simple Math

# read input
C = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))

metres = 0

for i in range(len(row1)):
    
    if row1[i] == 1:
        metres = metres + 3
    if row2[i] == 1:
        metres = metres + 3
        
    if i % 2 == 0:
        if row1[i] == 1 and row2[i] == 1:
            metres = metres - 2

    if i + 1 <= len(row1) - 1:
        if row1[i] == 1 and row1[i + 1] == 1:
            metres = metres - 2
        if row2[i] == 1 and row2[i + 1] == 1:
            metres = metres - 2


print(metres)
