from sympy import Symbol
import numpy as np


def newtonmethod(func1, func2, w, h, e, q, x, y, n):
    def f(x, y):
        f1 = eval(str(func1))
        f2 = eval(str(func2))
        li = list((f1, f2))
        return li

    def prf(x, y):
        prf_1_1 = eval(str(w))
        prf_1_2 = eval(str(h))
        prf_2_1 = eval(str(e))
        prf_2_2 = eval(str(q))
        li_1 = list((prf_1_1, prf_1_2, prf_2_1, prf_2_2))
        return li_1

    def prfdet(x, y):
        a = [[prf(x, y)[0], prf(x, y)[1]],
             [prf(x, y)[2], prf(x, y)[3]]]
        deta = np.linalg.det(a)

        a_x = [[f(x, y)[0], prf(x, y)[1]],
               [f(x, y)[1], prf(x, y)[3]]]
        deta_x = np.linalg.det(a_x)

        a_y = [[prf(x, y)[0], f(x, y)[0]],
               [prf(x, y)[2], f(x, y)[1]]]
        deta_y = np.linalg.det(a_y)
        listdets = list((deta, deta_x, deta_y))
        return listdets

    for itercept in range(1, n):
        i_1 = x - (prfdet(x, y)[1] / prfdet(x, y)[0])
        x = i_1
        i_2 = y - (prfdet(x, y)[2] / prfdet(x, y)[0])
        y = i_2
    print("x =", x, "y =", y)


x = Symbol('x')
y = Symbol('y')
a = eval(input())
b = eval(input())
r1 = a.diff(x)
r2 = a.diff(y)
r3 = b.diff(x)
r4 = b.diff(y)
newtonmethod(a, b, r1, r2, r3, r4, -0.5, 2, 10)
