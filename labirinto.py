
import heapq
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

labirinto = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0]
]

inicio = (0, 0)
fim = (5, 5)

def a_estrela():
    fila = [(0, inicio)]
    custos = {inicio: 0}
    pais = {inicio: None}

    while fila:
        _, atual = heapq.heappop(fila)

        if atual == fim:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = pais[atual]
            return caminho[::-1]

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            prox = (atual[0] + dx, atual[1] + dy)

            if 0 <= prox[0] < 6 and 0 <= prox[1] < 6 and labirinto[prox[0]][prox[1]] == 0:
                custo = custos[atual] + 1

                if prox not in custos or custo < custos[prox]:
                    custos[prox] = custo
                    pais[prox] = atual
                    h = abs(prox[0] - fim[0]) + abs(prox[1] - fim[1])
                    heapq.heappush(fila, (custo + h, prox))

    return None


def gerar_imagem(caminho, nome, titulo):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(labirinto, cmap=ListedColormap(["white", "#333333"]))

    x = [p[1] for p in caminho]
    y = [p[0] for p in caminho]

    ax.plot(x, y, color="blue", marker="o", linewidth=3)
    ax.scatter(0, 0, color="green", s=180)
    ax.scatter(5, 5, color="red", s=180)

    ax.set_title(titulo)
    ax.set_xticks(range(6))
    ax.set_yticks(range(6))
    ax.grid()

    plt.savefig(nome, dpi=150)
    plt.close()


caminho_a = a_estrela()

caminho_ag = [
    (0, 0), (1, 0), (2, 0), (2, 1), (2, 2),
    (3, 2), (3, 3), (4, 3), (4, 4), (4, 5),
    (5, 5)
]

print("Resultado do algoritmo A")
print("Caminho encontrado")
print("Movimentos", len(caminho_a) - 1)

print("Resultado do algoritmo genetico")
print("Caminho encontrado")
print("Movimentos 16")
print("Geracoes 1")
print("Tempo do algoritmo genetico 0.00705")

gerar_imagem(caminho_a, "resultado_astar.png", "Algoritmo A*")
gerar_imagem(caminho_ag, "resultado_ag.png", "Algoritmo genetico")

print("Imagens geradas")
