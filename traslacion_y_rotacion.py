"Robotica Industrial"

import matplotlib.pyplot as plt

import numpy as np


# valores iniciales

x1 = 0

y1 = 0

vox = 25

voy = 0


def rotar(angulo):

    phi = np.radians(angulo)

    x2 = vox*np.cos(phi) - voy*np.sin(phi)

    y2 = voy*np.cos(phi) + vox*np.sin(phi)

    return x2, y2


def trasladar(x, y, dx, dy):

    return x + dx, y + dy


# Limitaremos la pantalla hasta 6 unidades en "y" y en "x"

plt.ylim(0, 30)

plt.xlim(0, 30)


# programa principal

x1, y1 = trasladar(x1, y1, 3, 3)  # Implementar la función trasladar


i = 0

for i in range(90):  # Rotamos 90 grados

    v1x, v1y = rotar(i)

    plt.plot([x1, v1x], [y1, v1y])  # vector nuevo por cada i


plt.show()
