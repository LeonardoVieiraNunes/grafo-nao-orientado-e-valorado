from Grafo import Grafo
from buildGrafo import buildGrafo


def dijkstra(gfo, s):
    caminhos = [[] for i in range(gfo.qtdVertices())]
    verticesVisitados = [False] * gfo.qtdVertices()
    distanciasVertices = [float('inf')] * gfo.qtdVertices()
    global c
    c = [[float('inf') for i in range(gfo.qtdVertices())] for j in range(gfo.qtdVertices())]
    for i in range(gfo.qtdVertices()):
        for j in range(gfo.qtdVertices()):
            if gfo.adj[i][j] != float('inf'):
                c[i][j] = False

    distanciasVertices[s-1] = 0
    caminhos[s-1].append(s)

    while False in verticesVisitados:

        (u, pu) = menorVertice(gfo, distanciasVertices, verticesVisitados)

        verticesVisitados[u-1] = True

        vizinhoNodes = gfo.vizinhos(u)
        vizinhoNodesNaoVisitado = list(filter(lambda v: verticesVisitados[v-1] == False, vizinhoNodes))

        for vert in vizinhoNodesNaoVisitado:
            if (distanciasVertices[vert-1] > gfo.peso(u,vert) + pu):
                distanciasVertices[vert-1] = gfo.peso(u,vert) + pu
                caminhos[vert-1] = caminhos[u-1] + [vert]


    for i in range(gfo.qtdVertices()):
        print(f'{gfo.vertices[i][0]}: {",".join(str(x) for x in caminhos[i])}; d={distanciasVertices[i]}')

def menorVertice(gfo, distanciasVertices, verticesVisitados):
    v = float('inf')

    for i in range(len(verticesVisitados)):
        if verticesVisitados[i] == False and v > distanciasVertices[i]:
            v = i
    peso = distanciasVertices[v]

    return (v+1, peso)

# g1 = Grafo()

# vertices = [1,2,3,4,5,6]
# arestas = [(1,2,2),(1,3,1),(2,4,1),(3,4,3),(3,5,4),(4,6,2),(5,6,2)]

# g1.addVertices(vertices)
# g1.addArestas(arestas)
# dijkstra(g1, 2)

def test():
    vertices = [1,2,3,4,5,6,7,8,9,10]
    arestas = [(1,2,350),(1,4,4100),(1,9,8300),(1,10,3700),(2,10,6600),(2,3,6000),(3,7,5600),(3,8,4900),(3,9,9500),(4,5,1500),(4,10,2000),(5,6,8800),(5,10,3100),(7,8,3400),(7,9,12500),(8,9,12000),(9,10,14000)]

    g1 = Grafo()
    g1.addVertices(vertices)
    g1.addArestas(arestas)
    dijkstra(g1, 6)

test()