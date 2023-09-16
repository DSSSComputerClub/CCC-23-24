# Author: Deon Jerom
# Date: Sept. 2023
# Solution to 2015 J5 π-day
# Problem Type -> Dynamic Programming

def dynamic(target_sum, k_people):
    dp = [[0 for _ in range(k_people+1)] for _ in range(target_sum+1)]
    dp[0][0] = 1
    for i in range(target_sum+1):
        for j in range(1, k_people+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-j][j]
    return dp[target_sum][k_people]

numb_pies = int(input())
k_people = int(input())
print(dynamic(numb_pies, k_people))
