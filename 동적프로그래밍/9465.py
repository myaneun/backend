"""첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 n (1 ≤ n ≤ 100,000)이 주어진다. 
다음 두 줄에는 n개의 정수가 주어지며, 각 정수는 그 위치에 해당하는 스티커의 점수이다. 
연속하는 두 정수 사이에는 빈 칸이 하나 있다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다. """
import sys
imput = sys.stdin.readline
T = int(input())
for _ in range(T): #T+1 아님
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)] #행=0,1

    if n>1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

    for i in range(2, n): #n+1아님
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])
        dp[1][i] += max(dp[0][i-1], dp[0][i-2])
    
    print(max(dp[0][n-1], dp[1][n-1]))