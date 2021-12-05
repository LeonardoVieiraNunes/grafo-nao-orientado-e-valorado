from Grafo import Grafo
from lerEntrada import grafoDeEntrada

def dijkstra(gfo: Grafo, s):
    distanciaVertices = [float('inf') for i in range(gfo.qtdVertices())]
    ancestral = [None for i in range(gfo.qtdVertices())]
    verticesVisitados = [False for i in range(gfo.qtdVertices())]
    caminhos = [[] for i in range(gfo.qtdVertices())]
    distanciaVertices[s-1] = 0
    caminhos[s - 1].append(s)
    while False in verticesVisitados:

        u = menorVertice(distanciaVertices, verticesVisitados)
        verticesVisitados[u] = True

        vizinhosNaoVisitados = list(filter(lambda vt: verticesVisitados[vt-1] == False, gfo.vizinhos(u+1)))

        for v in vizinhosNaoVisitados:
            if distanciaVertices[v - 1] > distanciaVertices[u] + gfo.peso(v, u+1):
                distanciaVertices[v - 1] = distanciaVertices[u] + gfo.peso(v, u+1)
                caminhos[v-1] = caminhos[u-1] + [v]
                ancestral[v - 1] = u+1

    return distanciaVertices, ancestral, caminhos


def menorVertice(distanciaVertices, verticesVisitados):
    greater = float('inf')
    for i in range(len(distanciaVertices)):
        if verticesVisitados[i] == False and distanciaVertices[i] < greater:
            greater = i

    return greater

def formatarDijkstra(caminhos,distancias):
    for i in range(len(caminhos)):
        stringpath = ''.join(str(v)+',' for v in caminhos[i]).strip(",")
        print(f"{i+1}: {stringpath}; d={distancias[i]}")

if __name__ == "__main__":
    g1 = grafoDeEntrada('casos-de-teste/fln_pequena.txt')
    dist, ancestrais, caminhos = dijkstra(g1, 6)
    formatarDijkstra(caminhos,dist)