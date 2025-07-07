import numpy as np

import matplotlib.pyplot as plt


# Constantes
g = 9.8 

# Parámetros iniciales
y0 = 1
v0 = 0
gammas = {
    'Hormiga': 6.54,
    'Persona': 0.235,
    'Auto': 0.0105
}

# Vector de tiempo
t = np.linspace(0, 2, 300)


def y_exacta(t, y0, v0, gamma):

    term1 = -g * t / gamma

    term2 = -1/gamma * (v0 + g/gamma) * (np.exp(-gamma * t) - 1)

    return y0 + term1 + term2


def y_taylor(t, y0, v0, gamma):

    a0 = -gamma * v0 - g

    return y0 + v0 * t + 0.5 * a0 * t**2


def y_libre(t, y0, v0):

    return y0 + v0 * t - 0.5 * g * t**2


# Calcular las curvas

y_roz = y_exacta(t, y0, v0, gammas['Auto'])

y_taylor2 = y_taylor(t, y0, v0, gammas['Auto'])

y_sin_roz = y_libre(t, y0, v0)


# Gráfico

plt.figure(figsize=(8,5))

plt.plot(t, y_roz, label="Exacta con rozamiento", color="blue")

plt.plot(t, y_taylor2, label="Taylor orden 2", color="red", linestyle="--")

plt.plot(t, y_sin_roz, label="Sin rozamiento", color="green", linestyle=":")

plt.title("Comparación: Exacta vs Taylor vs Sin rozamiento")

plt.xlabel("Tiempo (s)")

plt.ylabel("Altura (m)")

plt.legend()

plt.grid(True)

plt.show()

