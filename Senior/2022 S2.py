# Author: Deon
# Date: Sept. 2023
# Solution to 2022 S2 Good Groups
# Problem Type -> Implementation

from collections import defaultdict

# Read input
n = int(input())
same_group = defaultdict(set)
for _ in range(n):
    a, b = input().split()
    same_group[a].add(b)

m = int(input())
not_same_group = defaultdict(set)
for _ in range(m):
    a, b = input().split()
    not_same_group[a].add(b)


k = int(input())
count = 0
for _ in range(k):
    group = tuple(input().split())
    # Check for good groups
    for name in group:
        if name in same_group:
            count += sum(1 for value in same_group[name] if not value in group)
        if name in not_same_group:
            count += sum(1 for value in not_same_group[name] if value in group)

print(count)
