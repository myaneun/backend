import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a = sorted(a)

for i in range(len(a)):
    print(a[i])