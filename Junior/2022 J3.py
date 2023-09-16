# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2022 J3 Harp Tuning
# Problem Type -> Implementation

sequence = list(input())
for i, x in enumerate(sequence):
    if x == '+':
        sequence[i] = 'tighten'
    elif x == '-':
        sequence[i] = 'loosen'

for tune in range(len(sequence)):
    if tune > 0:
        if sequence[tune].isalpha() and sequence[tune - 1].isnumeric():
            print('')
    if sequence[tune] == 'tighten' or sequence[tune] == 'loosen':
        print(f' {sequence[tune]} ', end="")
    else:
        print(sequence[tune], end="")
