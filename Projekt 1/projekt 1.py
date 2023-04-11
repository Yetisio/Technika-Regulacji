import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

# numer indeksu
a = 2
b = 4   # id = 202 wiec b = 0 zamienia sie na b = 2+2
c = 2

def dSdt(t,S):
    y,v,x=S
    return [v,
            x,
            math.exp(-0.5*t)+(2*b+a)*x-(b*b+c+2*b*a)*v+a*(b*b+c)*y]

# warunki poczatkowe niezerowe

y0 = 0
v0 = 0
x0 = 1
S0 = [y0, v0, x0]

t = np.linspace(0, 1, 100)
sol = odeint(dSdt, y0=S0, t=t, tfirst=True)

plt.plot(t, sol.T[0])
plt.show()