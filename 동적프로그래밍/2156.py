"""첫째 줄에 포도주 잔의 개수 n이 주어진다. 
(1 ≤ n ≤ 10,000) 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다. 
포도주의 양은 1,000 이하의 음이 아닌 정수이다."""
import sys
input = sys.stdin.readline

n=int(input())
w=[0]*10000
d=[0]*10000
for i in range(n):
    w[i] = int(input())
d[0]=w[0]
d[1] = w[0]+w[1]
d[2] = max(w[2]+w[1], w[2]+w[0])
for i in range(3, n):
    d[i] = max(w[i]+d[i-2], w[i]+w[i-1]+d[i-3], d[i-1]) 
print(max(d))