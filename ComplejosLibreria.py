from math import sin, cos, atan


def suma(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def producto(c1, c2):
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])


def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])


def conjugado(c):
    return (c[0], -c[1])


def division(c1, c2):
    den = producto(c2, conjugado(c2))
    num = producto(c1, conjugado(c2))

    return (num[0]/den[0], num[1]/den[0])


def modulo(c):
    return (c[0] ** 2 + c[1] ** 2) ** (1 / 2)


def fase(c):
    PI = 3.14159265359
    if c[0] >= 0 and c[1] >= 0:

        return (atan(c[1] / c[0]))
    elif c[0] < 0 and c[1] >= 0:

        return (atan(c[1] / c[0])) + PI
    elif c[0] < 0 and c[1] < 0:

        return (atan(c[1] / c[0])) + PI
    elif c[0] >= 0 and c[1] < 0:

        return (atan(c[1] / c[0])) + 2 * PI


def cart_a_pol(c):
    return (modulo(c), fase(c))


def pol_a_cart(c):
    return (round(c[0] * cos(c[1]), 2), round(c[0] * sin(c[1]), 2))
