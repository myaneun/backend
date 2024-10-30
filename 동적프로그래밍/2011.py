import sys
input = sys.stdin.readline

N = list(map(int, input().rstrip()))


dp = [0]*(len(N)+1)
dp[0] = 1
dp[1] = 1

if N[0] == 0:
    print(0)
else:
    for i in range(1, len(N)):
        j = i+1 #dp의 인덱스

        if N[i] > 0:
            dp[j] += dp[j-1]
        if(10 <= 10*N[i-1] + N[i] <= 26):
            dp[j] += dp[j-2]
    print(dp[-1]%1000000)