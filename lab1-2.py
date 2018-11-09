def bisect(a, b, eps, f):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return 0
    while b - a > eps:
        dx = (b - a)/2
        x = a + dx
        if f(a)/f(x) < 0:
            b = x
        else:
            a = x
        return x


def chord(a, b, eps, f):
    while abs(b - a) > eps:
        a = b - (b - a) * f(b) / (f(b) - f(a))
        b = a + (a - b) * f(a) / (f(a) - f(b))
    return b


def newton(x0, f, f1, eps):
    x0 = float(x0)
    while True:
        x1 = x0 - (f(x0) / f1(x0))
        if abs(x1 - x0) < eps:
            return x1
        x0 = x1


print(bisect(-2, 3, 0.001, f=lambda x: (x**3 - 3 * x**2 - x + 4)))