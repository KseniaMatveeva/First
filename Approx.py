# Аппроксимировать сигнал, представляющий собой половину периода синусоиды амплитудой прямоугольным импульсом входные данные - сигнал, представляющий собой половину периода синусоиды выходные данные - аппроксимирующий прямоугольный импульс
In [1]:
from sympy import *

A = symbols("A")
B = symbols("B")
T = symbols("T")
t = symbols("t")
metrika = integrate((A*sin((pi/T)*t) - B)**2, (t, 0, T))

d = diff(metrika, B)

f = solve(d, B)

r = lambdify(A,f[0])

r(1)