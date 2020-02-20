n = int(input())

A = list(map(int, input().split()))
res = 0
for i in range(n):
    if A[i] > 0:
        res += 1
print(res)