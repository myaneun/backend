import sys
input = sys.stdin.readline

T = int(input())
p = [1,1,1,2,2]

for _ in range(95):
    p.append(p[-1]+p[-5])

for _ in range(T):
    N = int(input())
    print(p[N-1])

