print("Enter number: ")
num  = int(input())
print("Enter base: ")
base = int(input())
res = ""
while(num > 0):
    res = str(num % base) + res
    num  //= base
res = int(res)
print(res)