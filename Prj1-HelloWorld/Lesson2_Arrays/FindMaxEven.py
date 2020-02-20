print("Введите длину массива:")
n = int(input())
A = [0] * n
print("Введите элементы:")
for i in range(n):
    A[i] = int(input())
max = int(0)
for i in range(n):
    if(A[i] % 2 == 0 and A[i] > max):
        max = A[i]
print("Макс. четное: " + str(max))