from Grafo import Grafo
from lerEntrada import grafoDeEntrada
import numpy as np


class CFC:
    def __init__(self):
        self.tempoDfs = 0
        self.tempoDfsAdaptado = 0
        self.listaCFC = []

    def encontrarEncadeamento(self, conjunto: set, ancestralT: dict):
        raiz = conjunto[-1]
        for key, value in ancestralT.items():
            if value == raiz:
                conjunto.append(key)
                self.encontrarEncadeamento(conjunto, ancestralT)

    def formatCFC(self, ancestralT):
        for key, value in ancestralT.items():
            if value is None:
                self.listaCFC.append([key])
                self.encontrarEncadeamento(self.listaCFC[-1], ancestralT)
        for cfc in self.listaCFC:
            print(str(cfc)[1:-1])

    def dfsVisit(self, gfo: Grafo, v, verticesVisitados, tInicio, tFim, ancestral, isAdaptado=False):
        verticesVisitados[v] = True
        if isAdaptado:
            self.tempoDfsAdaptado += 1
            tInicio[v] = self.tempoDfsAdaptado
            for u in gfo.vizinhos(v):
                if verticesVisitados[u] is False:
                    ancestral[u] = v
                    self.dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral, isAdaptado=True)

            self.tempoDfsAdaptado += 1
            tFim[v] = self.tempoDfsAdaptado
        else:
            self.tempoDfs += 1
            tInicio[v] = self.tempoDfs
            for u in gfo.vizinhos(v):
                if verticesVisitados[u] is False:
                    ancestral[u] = v
                    self.dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral)

            self.tempoDfs += 1
            tFim[v] = self.tempoDfs

    def dfs(self, gfo: Grafo, tFimOrdenado=False):
        verticesVisitados, tInicio, tFim, ancestral = dict(), dict(), dict(), dict()
        for v in gfo.get_id_vertices():
            verticesVisitados[v] = False
            tInicio[v] = float('inf')
            tFim[v] = float('inf')
            ancestral[v] = None

        if tFimOrdenado:
            for u in tFimOrdenado:
                if verticesVisitados[u] is False:
                    self.dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral, isAdaptado=True)
        else:
            for u in gfo.get_id_vertices():
                if verticesVisitados[u] is False:
                    self.dfsVisit(gfo, u, verticesVisitados, tInicio, tFim, ancestral)

        return verticesVisitados, tInicio, tFim, ancestral

    def execute(self, gfo: Grafo):
        verticesVisitados, tInicio, tFim, ancestral = self.dfs(gfo)
        arcosT = np.matrix.tolist(np.transpose(gfo.adj))

        gfoT = Grafo()
        gfoT.vertices = gfo.vertices
        gfoT.adj = arcosT

        tFimOrdenado = list(dict(sorted(tFim.items(), key=lambda item: item[1], reverse=True)).keys())
        verticesVisitadosT, tInicioT, tFimT, ancestralT = self.dfs(gfoT, tFimOrdenado)
        self.formatCFC(ancestralT)


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/exemplo-cfc.txt", isDirigido=True)
    CFC().execute(g1)
