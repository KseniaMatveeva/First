
#Задание 2 Включить сигнал с помощью функции единичного скачка входные данные: сигнал (любой), время включения выходные - отфильтрованный сигнал

import scipy as sp

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

import math

from sympy import *
init_printing()
A = 1
w = 0.1
s = sp.array([A*sp.cos(w*t) for t in range(-20, 20)])
step = sp.array([1 if t >0 else 1/2 if t==0 else 0  for t in range(-20,20)])
result =step*s
plt.plot(step)
plt.plot(s)
plt.plot(result)
#исходный - синий
#выходной - рыжий

import scipy as sp

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt

import math

from sympy import *
init_printing()
A = 1
w = 0.1
s = sp.array([A*sp.cos(w*t) for t in range(-20, 50)])
step = sp.array([1 if (t-10)>0 else 1/2 if (t-10)==0 else 0  for t in range(-20,50)])
result =step*s
plt.plot(result)
plt.plot(step)

