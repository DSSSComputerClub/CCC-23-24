# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2020 J3 Art
# Problem Type -> Implementation

x_list = []
y_list = []
for _ in range(int(input())):
    a, b = input().split(',')
    x_list.append(int(a))
    y_list.append(int(b))

x_list = [i for i in x_list if (i >=0)]
y_list = [i for i in y_list if (i >=0)]
x_list.sort()
y_list.sort()


print(f'{x_list[0]-1},{y_list[0]-1}')
print(f'{x_list[-1]+1},{y_list[-1]+1}')
