import numpy as np
import matplotlib.pyplot as plt

G = -6.67430e-11 
M = 5.972e24    
RT = 6.371e6     

def f(r):
    return G * M / r**2

def f_prime(r):
    return -2 * G * M / r**3

def f_double_prime(r):
    return 6 * G * M / r**4

# Taylor de orden 2 centrado en r0 = RT
def polinomio_taylor_2(r):
    h = r - RT
    return f(RT) + f_prime(RT) * h + 0.5 * f_double_prime(RT) * h**2

# Alejar la gráfica: aumentar el rango de -1 millón a +1 millón de metros
r_values = np.linspace(RT - 1e6, RT + 1e6, 1000)
f_values = f(r_values)
polinomio_taylor_2_values = polinomio_taylor_2(r_values)

plt.figure(figsize=(12, 8))
plt.plot(r_values - RT, f_values, label='f(r) = -GM / r² (Gravitación)', color='blue', linewidth=2)
plt.plot(r_values - RT, polinomio_taylor_2_values, label='P₂(r): Taylor orden 2 en r₀ = RT', linestyle='--', color='red', linewidth=2)

# Agregar líneas de referencia
plt.axhline(y=f(RT), color='gray', linestyle=':', alpha=0.7, label=f'f(RT) = {f(RT):.2f} m/s²')
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.7, label='r = RT')

plt.xlabel('Altura sobre RT (m)', fontsize=12)
plt.ylabel('Aceleración gravitatoria (m/s²)', fontsize=12)
plt.title('Aproximación de f(r) cerca de RT usando polinomio de Taylor de orden 2\n(Vista alejada: ±1,000 km)', fontsize=14)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

# Mejorar el formato de los ejes
plt.ticklabel_format(style='scientific', axis='both', scilimits=(0,0))

plt.tight_layout()
plt.show()

# Información adicional
print(f"Radio de la Tierra (RT): {RT:.0f} m = {RT/1000:.1f} km")
print(f"Aceleración gravitatoria en la superficie: {f(RT):.2f} m/s²")
print(f"Rango graficado: ±{1e6/1000:.0f} km alrededor de RT")
print(f"Diferencia máxima entre función y Taylor: {np.max(np.abs(f_values - polinomio_taylor_2_values)):.3e} m/s²")
