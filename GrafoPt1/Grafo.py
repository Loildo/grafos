

class MatrizAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, v1, v2):
        self.matriz[v1-1][v2-1] = 1
        self.matriz[v2-1][v1-1] = 1  # Para grafos não direcionados

    def remover_aresta(self, v1, v2):
        self.matriz[v1-1][v2-1] = 0
        self.matriz[v2-1][v1-1] = 0

    def exibir(self):
        for linha in self.matriz:
            print(linha)


class MatrizIncidencia:
    def __init__(self, num_vertices, num_arestas):
        self.num_vertices = num_vertices
        self.num_arestas = num_arestas
        self.matriz = [[0] * num_arestas for _ in range(num_vertices)]
        self.arestas = 0

    def adicionar_aresta(self, v1, v2):
        if self.arestas >= self.num_arestas:
            raise IndexError("Número máximo de arestas atingido")
        self.matriz[v1][self.arestas] = 1
        self.matriz[v2][self.arestas] = 1  # Para grafos não direcionados
        self.arestas += 1

    def exibir(self):
        for linha in self.matriz:
            print(linha)


class ListaAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, v1, v2):
        self.lista[v1].append(v2)
        self.lista[v2].append(v1)  # Para grafos não direcionados

    def exibir(self):
        for vertice in range(self.num_vertices):
            print(f"{vertice}: {self.lista[vertice]}")
