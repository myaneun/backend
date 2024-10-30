import sys
input = sys.stdin.readline

n = int(input())
a = []
for _ in range(n):
    [age, name] = map(str, input().split())
    a.append([int(age), name])
for i in sorted(a, key=lambda x: x[0]): #나이를 기준으로 정렬하라는 의미
    print(i[0], i[1])