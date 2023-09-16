# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2016 J3 Hidden Palindrome
# Problem Type -> Implementation

length = []
word = str(input())

if word == word[::-1]:
    print(len(word))
else:
    for i in range(0, len(word), 1):
        begin = word[i]
        for x in range(len(word) - 1,  i, -1):
            end = word[x]
            if begin == end:
                s = word[i:x+1]
                if s == s[::-1]:
                    length.append(len(s))
    length.sort()
    print(length[-1])
