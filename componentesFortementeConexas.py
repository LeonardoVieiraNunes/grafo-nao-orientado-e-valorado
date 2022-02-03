from Grafo import Grafo
from lerEntrada import grafoDeEntrada
import numpy as np

def dfsAdaptado(gfo: Grafo, tFimOrdenado):
    verticesVisitadosT, tInicioT, tFimT, ancestralT = dict(), dict(), dict(), dict()
    for v in gfo.get_id_vertices():
        verticesVisitadosT[v] = False
        tInicioT[v] = float('inf')
        tFimT[v] = float('inf')
        ancestralT[v] = None

    tempo = 0

    for u in tFimOrdenado:
        if verticesVisitadosT[u] is False:
            dfsVisit(gfo, u, verticesVisitadosT, tInicioT, tFimT, ancestralT, tempo)

    return verticesVisitadosT, tInicioT, tFimT, ancestralT


def dfsVisit(gfo: Grafo, v, verticesVisitados, tInicio, tFim, ancestral, tempo):
    verticesVisitados[v] = True
    tempo += 1
    tInicio[v] = tempo
    for u in gfo.vizinhos(v):
        if verticesVisitados[u] is False:
            ancestral[u] = v
            dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral, tempo)

    tempo += 1
    tFim[v] = tempo


def dfs(gfo: Grafo):
    verticesVisitados, tInicio, tFim, ancestral = dict(), dict(), dict(), dict()
    for v in gfo.get_id_vertices():
        verticesVisitados[v] = False
        tInicio[v] = float('inf')
        tFim[v] = float('inf')
        ancestral[v] = None

    tempo = 0

    for u in gfo.get_id_vertices():
        if verticesVisitados[u] is False:
            dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral, tempo)

    return verticesVisitados, tInicio, tFim, ancestral


def componentesFortementeConexas(gfo: Grafo):
    verticesVisitados, tInicio, tFim, ancestral = dfs(gfo)
    arcosT = np.matrix.tolist(np.transpose(gfo.adj))

    gfoT = Grafo()
    gfoT.vertices = gfo.vertices
    gfoT.adj = arcosT

    tFimOrdenado = list(dict(sorted(tFim.items(), key=lambda item: item[1], reverse=True)).keys())
    verticesVisitadosT, tInicioT, tFimT, ancestralT = dfsAdaptado(gfo, tFimOrdenado)
    return ancestralT


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/exemplo-cfc.txt", isDirigido=True)
    a = componentesFortementeConexas(g1)
