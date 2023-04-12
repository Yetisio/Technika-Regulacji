import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint
# numer indeksu ABCabc=264202
a = 2
b = 4
c = 2
def dSdt(t,S):
    y,v,x=S
    return [v,
            x,
            math.exp(-0.5*t)+(2*b+a)*x-(b*b+c+2*b*a)*v+a*(b*b+c)*y]


def mojeObliczenia(t,S):
    y,v,x=S
    return [
        v,
        x,
        (math.exp(2*t)/15)-((8*math.exp(-0.5*t))/445)-(13/267)*math.exp(4*t)*math.cos(math.sqrt(2)*t)+(7/267*math.sqrt(2))*math.exp(4*t)*math.sin(math.sqrt(2)*t)+3*y*math.exp(2*t)-2*y*math.exp(4*t)*math.cos(math.sqrt(2)*t)+math.sqrt(2)*y*math.exp(4*t)*math.sin(math.sqrt(2)*t)-4*math.sqrt(2)*v*math.exp(2*t)+4*math.sqrt(2)*v*math.exp(4*t)-5*v*math.exp(4*t)*math.sin(math.sqrt(2)*t)+math.sqrt(2)*x*math.exp(2*t)-math.sqrt(2)*x*math.exp(4*t)*math.cos(math.sqrt(2)*t)+2*x*math.exp(4*t)*math.sin(math.sqrt(2)*t)
    ]
# warunki poczatkowe niezerowe
y0 = 2
v0 = 2
x0 = 2
S0 = [y0, v0, x0]

t = np.linspace(0, 1, 100)
sol = odeint(dSdt, y0=S0, t=t, tfirst=True)
solM= odeint(mojeObliczenia, y0=S0, t=t, tfirst=True)
plt.plot(t, sol.T[0],label='komputerowe')
plt.legend()
plt.show()
plt.plot(t, solM.T[0],label='kartka')
plt.legend()
plt.show()

