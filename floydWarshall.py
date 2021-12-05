import Grafo
from lerEntrada import grafoDeEntrada


def floydWarshall(gfo: Grafo):
    a = [[] for _ in range(gfo.qtdVertices())]
    for k in range(gfo.qtdVertices()):
        for i in range(gfo.qtdVertices()):
            for j in range(gfo.qtdVertices()):
                gfo.adj[i][j] = min(gfo.adj[i][j], gfo.adj[i][k] + gfo.adj[k][j])

    return gfo

def floydWarshallResult(gfo: Grafo):
    for i in range(gfo.qtdVertices()):
        print("%d: " % (i + 1) + ",".join(map(str, gfo.adj[i])))
    print("\ninf: repre senta uma aresta de peso infinito (não existe)")


if __name__ == "__main__":
    g = grafoDeEntrada('casos-de-teste/fln_pequena.txt')
    floydWarshallResult(floydWarshall(g))
