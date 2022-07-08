from cs50 import get_int

n = 0

while n<1 or n>8:
    n = get_int("Hight:")
k = n
for i in range(n):
    for j in range(k-1):
        print("", end=" ")
    k -= 1
    for j in range(i+1):
        print("#", end="")
    print("")