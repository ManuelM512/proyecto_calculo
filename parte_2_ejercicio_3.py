import numpy as np
import matplotlib.pyplot as plt

g = 9.8
gamma = 0.235 
vT = -g / gamma

casos = [
    ("Reposo", 0),
    ("Vel inicial arbitraria", -30),
    ("v0 = vT", vT)
]

# Tiempo de simulación
t = np.linspace(0, 20, 500)


def velocidad_con_rozamiento(t, v0, gamma):
    return -g / gamma + (v0 + g / gamma) * np.exp(-gamma * t)

def velocidad_sin_rozamiento(t, v0):
    return v0 - g * t


for nombre, v0 in casos:
    v_roz = velocidad_con_rozamiento(t, v0, gamma)
    v_sin = velocidad_sin_rozamiento(t, v0)

    plt.figure(figsize=(8,5))
    plt.plot(t, v_roz, label="Con rozamiento", color="blue")
    plt.plot(t, v_sin, label="Sin rozamiento", linestyle="--", color="green")
    plt.axhline(y=vT, color="red", linestyle=":", label="Velocidad terminal")
    plt.title(f"Velocidad vs Tiempo - {nombre} (v0 = {v0:.2f} m/s)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Velocidad (m/s)")
    plt.grid(True)
    plt.legend()
    plt.show()
