from random import randint


n = int(input("Enter n > "))
a = [0.0] * n

with open("test.txt", "r") as f:
    b = f.read().split(" ")

for i in range(0, n):
    a[i] = float(b[randint(0, len(b) - 1)])


print(a)
