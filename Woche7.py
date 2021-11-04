import numpy as np


def zufallsVariable(X, P, decimals=6):
    if len(X) != len(P):
        raise Exception(":(((((((((((")

    Ex = 0

    for i in range(len(X)):
        Ex += X[i] * P[i]

    Vx = 0

    for i in range(len(X)):
        Vx += (X[i] - Ex)**2 * P[i]

    Ex2 = Vx + Ex**2

    return np.round(Ex, decimals), \
           np.round(Ex2, decimals), \
           np.round(Vx, decimals)


Ex, Ex2, Vx = zufallsVariable([2,3,4,9], [.1,.3,.5,.1])

print(Ex)
print(Ex2)
print(Vx)
