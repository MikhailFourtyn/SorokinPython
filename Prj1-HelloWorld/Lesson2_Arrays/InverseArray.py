n = int(input())

A = list(map(int, input().split()))

mid = n // 2

for i in range(mid):
    temp = A[i]
    A[i] = A[n - i - 1]
    A[n - i - 1] = temp

for i in range(n):
    print(A[i], end = ' ')