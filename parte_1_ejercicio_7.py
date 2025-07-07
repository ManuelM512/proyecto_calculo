import numpy as np
import matplotlib.pyplot as plt

G = -6.67430e-11 
M = 5.972e24     

def f(r):
    return G * M / r**2

def f1(r):
    return -2 * G * M / r**3

def f2(r):
    return 6 * G * M / r**4

def f3(r):
    return -24 * G * M / r**5

r0 = 0.01 

def P2(r):
    h = r - r0
    return f(r0) + f1(r0)*h + 0.5*f2(r0)*h**2

def P3(r):
    h = r - r0
    return P2(r) + (1/6)*f3(r0)*h**3

r_vals = np.linspace(0.005, 0.02, 500)
f_vals = f(r_vals)
p2_vals = P2(r_vals)
p3_vals = P3(r_vals)

plt.figure(figsize=(10, 6))
plt.plot(r_vals, f_vals, label='f(r) = -GM / r²', color='blue')
plt.plot(r_vals, p2_vals, label='Polinomio de Taylor orden 2', linestyle='--', color='orange')
plt.plot(r_vals, p3_vals, label='Polinomio de Taylor orden 3', linestyle='-.', color='green')
plt.axvline(r0, color='gray', linestyle=':', label='Centro r₀ = 0.01 m')
plt.xlabel('r (m)')
plt.ylabel('f(r) [m/s²]')
plt.title('Aproximación de f(r) cerca de r₀ = 0.01 con Taylor orden 2 y 3')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
