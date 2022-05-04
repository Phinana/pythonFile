from math import sqrt


def A(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

x = A(5)
for i in A(5):
    print(i)