from math import exp, cos, pow

n: int = int(input("Enter n > "))
x: float = float(input("Enter x > "))


def multiplier(nn: int, xx: float) -> float:
    p: float = - exp(cos(abs(xx)))
    for k in range(2, nn + 1):
        p *= ((k - 1) / k) - exp(cos(abs(k * xx)))
    return p


result: float = pow(n, 1 / 3) * pow(x, 1 / 2) - multiplier(n, x)
print(result)
