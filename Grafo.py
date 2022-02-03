class Grafo:
    def __init__(self, isDirigido=False):
        self.isDirigido = isDirigido
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

    def get_id_vertices(self):
        ids = []
        for v in self.vertices:
            ids.append(v[0])
        return ids


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

    def addVertice(self, nro, rotulo=None):
        self.vertices.append((nro, rotulo))
        self.addLinhasEColunas()

    def addLinhasEColunas(self):
        
        self.adj.append([])

        self.adj[-1] = [float('inf')] * (len(self.vertices) - 1)

        for i in self.adj:
            i.append(float('inf'))

    def addVertices(self, vertices):
        for v in vertices:
            self.addVertice(v)
    
    def addArestas(self, arestas):
        for v in arestas:
            self.addAresta(v[0], v[1], v[2])

    def addAresta(self, v1, v2, peso=1):
        self.adj[v1-1][v2-1] = peso
        if not self.isDirigido:
            self.adj[v2-1][v1-1] = peso
        self.nroArestas += 1