import numpy as np
import matplotlib.pyplot as plt
from random import randint


colors = []
roots = {}
rootNumber = 0
X = np.arange(-1, 10, .02)
Y = np.arange(-1, 10, .02)
Y = Y*1J
X, Y = np.meshgrid(X, Y)
Z = X+Y

def function(x):
    return x**4 +1
def der_function(x):
    return 4*x**3
def newtonsMethod(func, funcprime, x0, recursion):
    x = [x0]
    i = 0
    while i<recursion :
        x.append(x[i]- func(x[i])/funcprime(x[i]))
        i = i+1
    return x[i]

for i in Z:
    for a in i:
        val = newtonsMethod(function, der_function, a, 50)
        print(roots.__contains__(val.__str__()))
        if(roots.__contains__(val.__str__())):
            plt.plot(np.real(a), np.imag(a), color=colors[roots.__getitem__(val.__str__())])
        else:
            colors.append('#%06X' % randint(0, 0xFFFFFF))
            roots[val.__str__()] = rootNumber
            # print("val", val, type(val), "val_str", val.__str__(), type(val.__str__()), "roots: ", roots)
            rootNumber = rootNumber+1
plt.show()



