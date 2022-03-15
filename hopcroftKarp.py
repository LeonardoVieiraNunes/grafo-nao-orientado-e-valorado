from lerEntrada import grafoDeEntrada
from Grafo import Grafo


class EmparelhamentoMaximo:
    def __init__(self, gfo: Grafo):
        self.gfo = gfo
        self.mate = dict()
        self.x = list()
        self.y = list()
        self.i = 1
        self.d = dict()

    def getSets(self):
        i = self.gfo.get_id_vertices()[0]
        self.x = [i]
        t = dict()
        for v in self.gfo.get_id_vertices():
            t[v] = False

        t[i] = True

        while False in t.values():
            vizinhos = self.gfo.vizinhos(i)
            if i in self.x:
                for v in vizinhos:
                    if not t[v]:
                        self.y.append(v)
                        t[v] = True
            elif i in self.y:
                for v in vizinhos:
                    if not t[v]:
                        self.x.append(v)
                        t[v] = True

            i = (i + 1) % len(self.gfo.vertices)

    def hopcroftKarp(self):

        for v in self.gfo.get_id_vertices():
            self.d[v] = float('inf')
            self.mate[v] = None

        m = 0
        self.getSets()

        while self.BFS():
            for x in self.x:
                if self.mate[x] is None:
                    if self.DFS(x):
                        m += 1


    def BFS(self):
        fila = []
        for v in self.x:
            if self.mate[v] is None:
                self.d[v] = 0
                fila.insert(0, v)
            else:
                self.d[v] = float('inf')
        self.d[-1] = float('inf')

        while fila:
            v = fila.pop()
            if self.d[v] < self.d[-1]:
                vizinhos = self.gfo.vizinhos(v)
                for vizinho in vizinhos:
                    if self.d[self.mate[vizinho]] == float('inf'):
                        self.d[self.mate[vizinho]] = self.d[v] + 1
                        fila.insert(0, self.mate[vizinho])

        return self.d[-1] != float('inf')

    def DFS(self, x):
        if x is not None:
            for v in self.gfo.vizinhos(x):
                if self.d[self.mate[v]] == self.mate[x] + 1:
                    if self.DFS()


if __name__ == '__main__':
    g1 = grafoDeEntrada("casos-de-teste/exemplo-edmonds-karp.txt")
    EmparelhamentoMaximo(g1).hopcroftKarp()
