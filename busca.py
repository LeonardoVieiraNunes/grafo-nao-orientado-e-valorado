from Grafo import Grafo
from lerEntrada import grafoDeEntrada


def formatBusca(distanciaVertices, ancestral):
    for i in range(max(distanciaVertices) + 1):
        print([x for x in enumerate(ancestral) if x == i])


def busca(gfo: Grafo, s: int):
    distanciaVertices = [float('inf') for i in range(gfo.qtdVertices())]
    ancestral = [None for i in range(gfo.qtdVertices())]
    verticesVisitados = [False for i in range(gfo.qtdVertices())]

    distanciaVertices[s - 1] = 0
    verticesVisitados[s - 1] = True

    filaVisitas = [s - 1]

    while len(filaVisitas) != 0:
        u = filaVisitas.pop(0)
        for v in gfo.vizinhos(u + 1):
            if not verticesVisitados[v - 1]:
                verticesVisitados[v - 1] = True
                distanciaVertices[v - 1] = distanciaVertices[u] + 1
                ancestral[v - 1] = u + 1
                filaVisitas = [v - 1] + filaVisitas
    return distanciaVertices, ancestral


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/busca.txt")
    d, a = busca(g1, 1)
    formatBusca(d, a)
