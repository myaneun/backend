import sys
input = sys.stdin.readline

n=int(input())
A=[0]*301
for i in range(1, n+1):
    A[i] = int(input())

d=[0]*301
d[1] = A[1]
d[2] = A[1]+A[2]
d[3] = max(A[1]+A[3], A[2]+A[3])

for i in range(4, n+1):
    d[i] = max(d[i-2]+A[i], d[i-3]+A[i-1]+A[i])

print(d[n])