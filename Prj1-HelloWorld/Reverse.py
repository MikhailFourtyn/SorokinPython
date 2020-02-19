a = int(input())
res = int(0)
while a > 0:
    res *= 10
    res += (a % 10)
    a = a // 10
print(int(res))
