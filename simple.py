from math import exp, cos, pow


n = int(input("Enter positive int n > "))
x = float(input("Enter x > "))


def multiplier(nn, xx):
    p = - exp(cos(abs(xx)))
    for k in range(2, nn + 1):
        p *= ((k - 1) / k) - exp(cos(abs(k * xx)))
    return p


result = pow(n, 1 / 3) * pow(x, 1 / 2) - multiplier(n, x)
print(result)
