import numpy as np

from Grafo import Grafo
from lerEntrada import grafoDeEntrada


class FluxoMaximo:
    def __init__(self, gfo: Grafo, source: int, target: int):
        self.gfo = gfo
        self.source = source
        self.target = target

    def execute(self):
        fluxoMaximo = 0
        source = self.source
        target = self.target
        while True:
            caminhoAumentante = self.edmonds_karp(source, target)

            if not caminhoAumentante:
                break

            fluxo_caminho = float('inf')

            for i in range(len(caminhoAumentante) - 1):
                fluxo_caminho = min(self.gfo.adj[caminhoAumentante[i]-1][caminhoAumentante[i + 1]-1],
                                    fluxo_caminho)

            for i in range(len(caminhoAumentante) - 1):
                self.gfo.adj[caminhoAumentante[i]-1][caminhoAumentante[i + 1]-1] -= fluxo_caminho
            fluxoMaximo += fluxo_caminho

        print(fluxoMaximo)

    def edmonds_karp(self, source, target):
        verticesVisitados = dict()
        ancestral = dict()
        fila = list()

        for v in self.gfo.get_id_vertices():
            verticesVisitados[v] = False
            ancestral[v] = None

        verticesVisitados[source] = True
        fila.append(source)

        while fila:
            u = fila.pop(0)
            for v in self.gfo.vizinhos(u):
                if verticesVisitados[v] is False and self.gfo.adj[u - 1][v - 1] > 0:
                    verticesVisitados[v] = True
                    ancestral[v] = u

                    if v == target:
                        caminhoAumentante = [target]
                        w = target
                        while w != source:
                            w = ancestral[w]
                            caminhoAumentante = [w] + caminhoAumentante
                        return caminhoAumentante
                    fila.append(v)
        return []


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/exemplo-edmonds-karp.txt", isDirigido=True)
    FluxoMaximo(g1, 1, 6).execute()
