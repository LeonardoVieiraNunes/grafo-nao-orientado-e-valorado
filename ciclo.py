from Grafo import Grafo


def cicloEureliano(gfo):
    global c
    c = [[float('inf') for i in range(gfo.qtdVertices())] for j in range(gfo.qtdVertices())]
    for i in range(gfo.qtdVertices()):
        for j in range(gfo.qtdVertices()):
            if gfo.adj[i][j] != float('inf'):
                c[i][j] = False

    (isSubCiclo, caminho) = buscarSubCicloEuleriano(gfo, 1, c)

    if not isSubCiclo:
        return (False, [])
    else:
        for v in c:
            if False in v:
                return (False, [])
            else:
                return (True, caminho)


def buscarSubCicloEuleriano(gfo, vert, c):
    caminho = [vert]
    t = vert

    while caminho.count(t) < 2:
        if False not in c[vert-1]:
            return (False, [])
        else:
            index = c[vert-1].index(False)
            c[vert-1][index] = True
            c[index][vert-1] = True

            vert = index + 1

            caminho.append(vert)

    vertNaoVisitado = set(filter(lambda v: False in c[v-1], caminho))
    for v in vertNaoVisitado:
        
        (isSubCiclo, subCaminho) = buscarSubCicloEuleriano(gfo, v, c)
        if not isSubCiclo:
            return (False, [])
        else:
            pos = caminho.index(v)
            before = caminho[:pos]
            after = caminho[pos+1:]
            caminho = before + subCaminho + after
            

    return (True, caminho)

g1 = Grafo()

arestasNe = [(1,2),(1,6),(2,3),(3,6),(3,4),(4,5)]
verticesNe = [1,2,3,4,5,6]

arestasCe = [(1,2),(1,6),(2,3),(3,6),(3,4),(3,5),(4,5)]
verticesCe = [1,2,3,4,5,6]

arestasTeste = [(1,2),(2,3),(3,4),(4,1),(2,5),(2,6),(5,6)]
verticesTeste = [1,2,3,4,5,6]

g1 = Grafo()
g1.addVertices(verticesCe)
g1.addArestas(arestasCe)

(isCicloEureliano, caminho) = cicloEureliano(g1)

if (isCicloEureliano):
    print(1)
    print(caminho)
else:
    print("não é um ciclo eureliano")

