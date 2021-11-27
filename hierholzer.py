from Grafo import Grafo
from lerEntrada import grafoDeEntrada


def hierholzer(gfo: Grafo):
    arestasVisitadas = {}
    for i in range(gfo.qtdVertices()):
        for j in range(gfo.qtdVertices()):
            if gfo.adj[i][j] != float('inf'):
                arestasVisitadas[i + 1, j + 1] = False

    if gfo.vizinhos(1) == 0:
        return False, None

    (r, ciclo) = buscarSubCicloEuleriano(gfo, 1, arestasVisitadas)

    if not r:
        return False, None
    elif False in list(arestasVisitadas.values()):
        return False, None
    else:
        return True, ciclo


def buscarSubCicloEuleriano(gfo, v, arestasVisitadas):
    ciclo = [v]
    t = v

    while True:
        verticesNaoVisitadosDeV = [j for (i, j), value in arestasVisitadas.items() if v == i and value is False]
        if len(verticesNaoVisitadosDeV) == 0:
            return False, None
        else:
            u = verticesNaoVisitadosDeV[0]
            arestasVisitadas[v, u] = True
            arestasVisitadas[u, v] = True
            v = u
            ciclo = ciclo + [v]
        if v == t:
            break

    verticesComArestasNaoVisitadas = [j for (i, j), value in arestasVisitadas.items() if value is False and i not in list(arestasVisitadas.keys())]

    for x in verticesComArestasNaoVisitadas:
        (rRec, cicloRec) = buscarSubCicloEuleriano(gfo, x, arestasVisitadas)

        if not rRec:
            return False, None
        else:
            pos = ciclo.index(v)
            before = ciclo[:pos]
            after = ciclo[pos + 1:]
            ciclo = before + cicloRec + after

    return True, ciclo


def test():
    g1 = grafoDeEntrada('casos-de-teste/contem-ciclo-euleriano.txt')
    (isCicloEureliano, caminho) = hierholzer(g1)
    print(isCicloEureliano, caminho)
