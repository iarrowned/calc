import math

n = int(input("Введите положительное значение int n > "))
x = float(input("Введите значение x > "))

p = - math.exp(math.cos(abs(x)))
for k in range(2, n + 1):
    p *= ((k - 1) / k) - math.exp(math.cos(abs(k * x)))

result = math.pow(n, 1 / 3) * math.pow(x, 1 / 2) - p
print(result)