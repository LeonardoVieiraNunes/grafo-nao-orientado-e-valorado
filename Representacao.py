# representação por matriz de adjacências
# g = [[inf, 8, inf, 9],[8, inf, inf, 5],[inf,inf,inf,7]]

# adj = []
# adj = [[0]]
# adj = [[0,0],[0,0]]

class Grafo:
    def __init__(self):
        self.nroArestas = 0
        self.vertices = []
        self.adj = []

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return self.nroArestas

    def grau(self, vert):
        pesos = list(p for p in self.adj[vert-1] if p != float('inf'))
        return len(pesos)

    def rotulo(self, vert):
        rotulo = self.vertices[vert-1][1]
        return rotulo

    def vizinhos(self, vert):
        pesoArestas = self.adj[vert-1]
        arestas = []
        for i in range(len(pesoArestas)):
            if pesoArestas[i] != float('inf'):
                arestas.append(i+1)

        return arestas

    def haAresta(self, v1, v2):
        return self.adj[v1-1][v2-1] != float('inf')

    def peso(self, v1, v2):
        return self.adj[v1-1][v2-1]

    def addVertice(self, nro, rotulo):
        self.vertices.append((nro, rotulo))
        self.addLinhasEColunas()

    def addLinhasEColunas(self):
        
        self.adj.append([])

        self.adj[-1] = [float('inf')] * (len(self.vertices) - 1)

        for i in self.adj:
            i.append(float('inf'))

    def addAresta(self, v1, v2, peso):
        self.adj[v1-1][v2-1] = peso
        # se a -- b tem peso x, então b -- a tem peso x tbm quando é não orientado, não?
        self.adj[v2-1][v1-1] = peso
        self.nroArestas += 1





# ---debug----
# g1 = Grafo()
# g1.addVertice(1, "A")
# g1.addVertice(2, "B")
# g1.addVertice(3, "C")
# # print(g1.adj)

# g1.addAresta(1, 1, 7)
# g1.addAresta(2, 1, 9)

# print(g1.adj)

# print(g1.grau(2))
# print(g1.rotulo(3))
# print(g1.vizinhos(1))
# print(g1.haAresta(1,2))
# print(g1.peso(1,2))






        
        