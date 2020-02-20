print("Введите длину массива: ")
n = int(input())
A = []
print("Введите элементы:")
for i in range(0, n):
    A.append(int(input()))
max = int(0)
for i in range(0, n):
    if A[i] > max:
        max = A[i]
print("Макс.: " + str(max))