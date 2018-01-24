# Отфильтровать сигнал с помощью дельта-функции Входные данные: сигнал(любой), время t дельта-функции Выходные - отфильтрованный сигнал

import scipy as sp
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
import math
from math import  exp
from sympy import *
init_printing()
a=15
b=100
c=17
d=100
# c шагом
s=[exp((-(a/b))*t) - exp(-((c/d))*t)for t in range(0,30)]
delta = sp.array([i if i==1 else 0 for i in range(0, 30)])
result = delta * s
plt.plot(s)
plt.plot(result)
#синий-вх
#оранж.-вых


