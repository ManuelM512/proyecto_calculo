import numpy as np
import pandas as pd

g = 9.8  
gammas = {
    'Hormiga': 6.54,
    'Persona': 0.235,
    'Auto': 0.0105
}

casos = [
    (1, 0),
    (1000, 0),
    (1, -100),
    (1000, -100),
    (0, 0.1),
    (0, 100)
]

def modelo_con_rozamiento(t, y0, v0, gamma):
    term1 = -g * t / gamma
    term2 = -1/gamma * (v0 + g/gamma) * (np.exp(-gamma * t) - 1)
    return y0 + term1 + term2

def modelo_sin_rozamiento(t, y0, v0):
    return y0 + v0 * t - 0.5 * g * t**2

def taylor_orden_2(t, y0, v0, gamma):
    a0 = -gamma * v0 - g
    return y0 + v0 * t + 0.5 * a0 * t**2

def generar_formula_con_rozamiento(y0, v0, gamma):
    """Genera la fórmula algebraica con rozamiento con parámetros sustituidos"""
    return f"{y0} + (-{g}*t/{gamma}) + (-1/{gamma})*({v0} + {g}/{gamma})*(exp(-{gamma}*t) - 1)"

def generar_formula_sin_rozamiento(y0, v0):
    """Genera la fórmula algebraica sin rozamiento con parámetros sustituidos"""
    return f"{y0} + {v0}*t - 0.5*{g}*t²"

def generar_formula_taylor(y0, v0, gamma):
    """Genera la fórmula algebraica de Taylor con parámetros sustituidos"""
    a0 = -gamma * v0 - g
    return f"{y0} + {v0}*t + 0.5*({a0})*t²"

def crear_tabla_por_gamma(gamma_nombre, gamma_valor):
    """Crea una tabla para un gamma específico con resultados por tiempo"""
    datos = []
    t_valores = [5, 10, 20]
    
    for i, (y0, v0) in enumerate(casos, 1):
        # Generar fórmulas algebraicas
        formula_roz = generar_formula_con_rozamiento(y0, v0, gamma_valor)
        formula_libre = generar_formula_sin_rozamiento(y0, v0)
        formula_taylor = generar_formula_taylor(y0, v0, gamma_valor)
        
        # Calcular resultados para cada tiempo
        resultados_t5 = []
        resultados_t10 = []
        resultados_t20 = []
        
        for t in t_valores:
            y_roz = round(modelo_con_rozamiento(t, y0, v0, gamma_valor), 3)
            y_libre = round(modelo_sin_rozamiento(t, y0, v0), 3)
            y_taylor = round(taylor_orden_2(t, y0, v0, gamma_valor), 3)
            
            if t == 5:
                resultados_t5 = f"[{y_roz}, {y_libre}, {y_taylor}]"
            elif t == 10:
                resultados_t10 = f"[{y_roz}, {y_libre}, {y_taylor}]"
            elif t == 20:
                resultados_t20 = f"[{y_roz}, {y_libre}, {y_taylor}]"
        
        datos.append({
            'Caso': i,
            'y₀ (m)': y0,
            'v₀ (m/s)': v0,
            'Formula_Con_Rozamiento': formula_roz,
            'Formula_Sin_Rozamiento': formula_libre,
            'Formula_Taylor_Orden_2': formula_taylor,
            't=5s [Roz, Libre, Taylor]': resultados_t5,
            't=10s [Roz, Libre, Taylor]': resultados_t10,
            't=20s [Roz, Libre, Taylor]': resultados_t20
        })
    
    return pd.DataFrame(datos)

def generar_tablas_separadas():
    """Genera una tabla CSV separada para cada gamma"""
    archivos_generados = []
    
    for gamma_nombre, gamma_valor in gammas.items():
        # Crear tabla para este gamma
        df_gamma = crear_tabla_por_gamma(gamma_nombre, gamma_valor)
        
        # Nombre del archivo
        nombre_archivo = f"tabla_{gamma_nombre.lower()}_gamma_{gamma_valor}.csv"
        
        # Guardar CSV
        df_gamma.to_csv(nombre_archivo, index=False, encoding='utf-8')
        archivos_generados.append(nombre_archivo)
    
    return archivos_generados

if __name__ == "__main__":
    archivos = generar_tablas_separadas()