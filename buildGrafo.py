def buildGrafo():
    g1 = Grafo()

    nroVertices = input("*vertices ")
    nroVertices = int(nroVertices)

    for i in range(nroVertices):
        n, rotulo = input().split()
        n = int(n)

        g1.addVertice(n, rotulo)
    print("*edges")
    while True:
        v1, v2, peso = input().split()
        if (v1 == v2 == peso == '-1'):
            break

        v1 = int(v1)
        v2 = int(v2)
        peso = int(peso)

        g1.addAresta(v1,v2,peso)

    return g1

