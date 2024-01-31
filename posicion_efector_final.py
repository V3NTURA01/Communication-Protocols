import numpy as np
import math

# Esta función crea la matriz de Denavit-Hartenberg con los parámetros proporcionados


def crear_matriz_dh(theta, d, a, alpha):
    # Se retorna la matriz DH
    return np.array([
        [math.cos(theta), -math.sin(theta) * math.cos(alpha),
         math.sin(theta) * math.sin(alpha), a * math.cos(theta)],
        [math.sin(theta), math.cos(theta) * math.cos(alpha), -
         math.cos(theta) * math.sin(alpha), a * math.sin(theta)],
        [0, math.sin(alpha), math.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Esta función calcula la posición del efector final utilizando las matrices DH


def obtener_posicion_efector(param_dh):
    matriz_total = np.eye(4)  # Se inicia con una matriz identidad
    for parametros in param_dh:
        theta, d, a, alpha = parametros
        matriz_actual = crear_matriz_dh(theta, d, a, alpha)
        # Se multiplica con la matriz actual
        matriz_total = np.matmul(matriz_total, matriz_actual)
    coordenadas = matriz_total[:3, 3]  # Se extraen las coordenadas
    return tuple(coordenadas)


# Principal
if __name__ == "__main__":
    parametros_dh = [
        (math.radians(60), 0, 150, 0),  # Primer eslabón
        (math.radians(45), 0, 150, 0),  # Segundo eslabón
        (0, 80, 0, 0),                  # Tercer eslabón
        (math.radians(90), 0, 0, 0)     # Cuarto eslabón
    ]

    # Se obtiene la posición del efector final
    x, y, z = obtener_posicion_efector(parametros_dh)
    # Se imprime la posición
    print(f"Posición del efector final: X = {x:.2f}, Y = {y:.2f}, Z = {z:.2f}")
