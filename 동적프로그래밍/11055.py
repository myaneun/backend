import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
d=[0]*n
d[0] = A[0]
for i in range(1, n):
    for j in range(i):
        if A[i]>A[j]:
            d[i] = max(d[i], d[j]+A[i])
        else:
            d[i] = max(d[i], A[i])
print(max(d))