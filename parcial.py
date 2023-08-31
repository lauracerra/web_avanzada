import math

#La función distancia(p1, p2) calcula la distancia euclidiana entre dos puntos.
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

#La función pares_cercanos_divide_y_venceras(coordenadas) implementa el enfoque de "Divide y Vencerás" para encontrar los puntos más cercanos. Si la cantidad de coordenadas es pequeña (3 o menos), se realiza una búsqueda exhaustiva para encontrar el par de puntos más cercanos y se devuelve la distancia y los puntos
def pares_cercanos_divide_y_venceras(coordenadas):
    if len(coordenadas) <= 3:
        min_dist = float('inf')
        puntos_mas_cercanos = ()
        for i in range(len(coordenadas)):
            for j in range(i+1, len(coordenadas)):
                dist = distancia(coordenadas[i], coordenadas[j])
                if dist < min_dist:
                    min_dist = dist
                    puntos_mas_cercanos = (coordenadas[i], coordenadas[j])
        return puntos_mas_cercanos, min_dist

    medio = len(coordenadas) // 2
    coordenadas_izquierda = coordenadas[:medio]
    coordenadas_derecha = coordenadas[medio:]

    pares_izquierda, dist_izquierda = pares_cercanos_divide_y_venceras(coordenadas_izquierda)
    pares_derecha, dist_derecha = pares_cercanos_divide_y_venceras(coordenadas_derecha)

    min_dist = min(dist_izquierda, dist_derecha)
    puntos_mas_cercanos = pares_izquierda if dist_izquierda <= dist_derecha else pares_derecha

    strip = []
    for punto in coordenadas:
        if abs(punto[0] - coordenadas[medio][0]) < min_dist:
            strip.append(punto)

    strip = sorted(strip, key=lambda x: x[1])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distancia(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                puntos_mas_cercanos = (strip[i], strip[j])
            j += 1

    return puntos_mas_cercanos, min_dist

def pares_cercanos(*args, **kwargs):
    coordenadas = args[0]
    coordenadas.sort(key=lambda x: x[0])
    return pares_cercanos_divide_y_venceras(coordenadas)

# Ejemplo de uso
puntos_mas_cercanos, distancia_minima = pares_cercanos([(1, 2), (3, 5), (8, 9), (10, 11), (15, 17)])
print("Puntos más cercanos:", puntos_mas_cercanos)
print("Distancia mínima:", distancia_minima)
