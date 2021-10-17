from math import exp, cos, pow

""" 
    Inputs: 
    n: positive int
    x: float or int
"""
check: bool = False
while not check:
    try:
        n: int = int(input("Enter positive int n > "))
        x: float = float(input("Enter x > "))
        if n < 0:
            raise ValueError
        check = True
    except ValueError:
        print("Enter correct values")


def multiplier(nn: int, xx: float) -> float:
    """
    :param nn: int, required
    :param xx: float or int, required
    :return: float, result of multiple loop
    """
    p: float = - exp(cos(abs(xx)))
    for k in range(2, nn + 1):
        p *= ((k - 1) / k) - exp(cos(abs(k * xx)))
    return p


result: float = pow(n, 1 / 3) * pow(x, 1 / 2) - multiplier(n, x)
print(result)
