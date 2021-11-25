from Grafo import Grafo
from lerEntrada import grafoDeEntrada

def hierholzer(gfo: Grafo):
    global arestasVisitadas
    arestasVisitadas = [[float('inf') for i in range(gfo.qtdVertices())] for j in range(gfo.qtdVertices())]
    for i in range(gfo.qtdVertices()):
        for j in range(gfo.qtdVertices()):
            if gfo.adj[i][j] != float('inf'):
                arestasVisitadas[i][j] = False

    if gfo.vizinhos(1) == 0:
        return False, None

    (r, ciclo) = buscarSubCicloEuleriano(gfo, 1, arestasVisitadas)


def buscarSubCicloEuleriano(gfo, v, arestasVisitadas):
    ciclo = [v]
    t = v

    while t == v:
        result = dict(map(lambda u: (u, arestasVisitadas[u - 1][v - 1]), gfo.vizinhos(v)))
        if True in list(result.values()):
            return False, None
        else:
            u = [key for key, value in result.items() if value is False][0]
            arestasVisitadas[v-1][u-1] = True
            v = u
            ciclo = ciclo + [v]

    verticesComArestasNaoVisitadas = set(filter(lambda v: False in arestasVisitadas[v-1], ciclo))

    for x in verticesComArestasNaoVisitadas:
        (rRec,cicloRec) = buscarSubCicloEuleriano(gfo, x, arestasVisitadas)

        if not rRec:
            return False, None
        else:
            pos = ciclo.index(v)
            before = ciclo[:pos]
            after = ciclo[pos + 1:]
            ciclo = before + cicloRec + after

    return True, ciclo



def test():
    g1 = grafoDeEntrada('casos-de-teste/fln_pequena.txt')
    (isCicloEureliano, caminho) = hierholzer(g1)