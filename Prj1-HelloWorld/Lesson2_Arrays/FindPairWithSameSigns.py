n = int(input())

A = list(map(int, input().split()))
res = "NO"
for i in range(1, n):
    if A[i] * A[i - 1] > 0:
        res = "YES"
print(res)