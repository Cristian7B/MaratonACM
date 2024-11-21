# ---------------- Mi version ----------------
def calcular():
    it = int(input())
    positions = []
    initial = [0, 0]
    effort = 0
    for _ in range(it):
        positions.append(list(map(int, input().split())))
    print(positions)
    for _ in range(len(positions)):
        iterD = {}
        for i in range(len(positions)):
            iterD[f"{positions[i][0]},{positions[i][1]}"] = (es(initial, positions[i][0], positions[i][1]))
        iterD = dict(sorted(iterD.items()))
        print(iterD)
        key = next(iter(iterD))
        effort += iterD[key]
        positions.remove(list(map(int, key.split(","))))
        initial = list(key)

    print(effort)
def es(i, x, y):
    return ((int(i[0]) - int(x))**2) + ((int(i[1]) - int(y))**2)

calcular()



# ---------------- Solucion ----------------
import heapq
def calcular_costo_minimo(n, puntos):
    # Creamos una cola de prioridad (heap) para las aristas
    heap = []
    # Lista para marcar los nodos visitados
    visitados = [False] * n
    # Coste total del Árbol de Expansión Mínima
    costo_total = 0
    # Nodos que ya hemos conectado
    nodos_conectados = 0

    # Añadimos el nodo inicial (el origen (0,0) no está en la lista de puntos)
    heapq.heappush(heap, (0, 0))  # (peso, índice del nodo)

    while nodos_conectados < n:
        # Extraemos la arista con el menor costo    
        peso, nodo_actual = heapq.heappop(heap)
        print(nodo_actual)

        # Si el nodo ya está visitado, continuamos
        if visitados[nodo_actual]:
            continue

        # Marcamos el nodo como visitado y lo añadimos al costo total
        visitados[nodo_actual] = True
        costo_total += peso
        nodos_conectados += 1

        # Exploramos los nodos vecinos
        for vecino in range(n):
            if not visitados[vecino]:
                # Calculamos el costo al vecino usando la distancia euclidiana al cuadrado
                dx = puntos[nodo_actual][0] - puntos[vecino][0]
                dy = puntos[nodo_actual][1] - puntos[vecino][1]
                distancia = dx**2 + dy**2
                heapq.heappush(heap, (distancia, vecino))

    return costo_total


# Entrada
n = int(input())  # Número de puntos
puntos = [tuple(map(int, input().split())) for _ in range(n)]

# Cálculo del costo mínimo
resultado = calcular_costo_minimo(n, puntos)

# Salida
print(resultado)
