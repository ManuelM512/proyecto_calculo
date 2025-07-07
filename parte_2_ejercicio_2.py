import numpy as np
import matplotlib.pyplot as plt

g = 9.8  
gammas = {
    'Hormiga': 6.54,
    'Persona': 0.235,
    'Auto': 0.0105
}


def modelo_con_rozamiento(t, y0, v0, gamma):
    term1 = -g * t / gamma
    term2 = -1/gamma * (v0 + g/gamma) * (np.exp(-gamma * t) - 1)
    return y0 + term1 + term2

def modelo_sin_rozamiento(t, y0, v0):
    return y0 + v0 * t - 0.5 * g * t**2

def taylor_orden_2(t, y0, v0, gamma):
    a0 = -gamma * v0 - g
    return y0 + v0 * t + 0.5 * a0 * t**2

casos = [
    (1, 0),
    (1000, 0),
    (1, -100),
    (1000, -100),
    (0, 0.1),
    (0, 100)
]

# Tiempo de simulación
t_max = 20
t = np.linspace(0, t_max, 500)

gamma_valor = gammas['Hormiga']

for i, (y0, v0) in enumerate(casos, 1):
    y_roz = modelo_con_rozamiento(t, y0, v0, gamma_valor)
    y_libre = modelo_sin_rozamiento(t, y0, v0)
    y_taylor = taylor_orden_2(t, y0, v0, gamma_valor)

    plt.figure(figsize=(8,5))
    plt.plot(t, y_roz, label="Con rozamiento", color="blue")
    plt.plot(t, y_libre, label="Sin rozamiento", color="green", linestyle='--')
    plt.plot(t, y_taylor, label="Taylor orden 2", color="red", linestyle=':')
    plt.title(f"Caída libre - Caso {i} | y₀={y0}, v₀={v0}, γ={gamma_valor}")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Altura (m)")
    plt.legend()
    plt.grid(True)
    plt.ylim(bottom=min(y_roz.min(), y_libre.min(), y_taylor.min()) - 10)
    plt.show()
