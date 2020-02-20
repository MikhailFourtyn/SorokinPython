n = int(input())

A = list(map(int, input().split()))

for i in range(1, n, 2):
    temp = A[i - 1]
    A[i - 1] = A[i]
    A[i] = temp

for i in range(n):
    print(A[i], end = ' ')