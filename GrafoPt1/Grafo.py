

class MatrizAdjacencia:
    def __init__(self, num_vertices):
        self.qtd_aresta = 0
        self.num_vertices = num_vertices
        self.matriz = [[0] * num_vertices for i in range(num_vertices)]

    def adicionar_aresta(self, v1, v2, ponderacao):
        self.qtd_aresta += 1 
        self.matriz[v1-1][v2-1] = ponderacao
        self.matriz[v2-1][v1-1] = ponderacao  # Para grafos não direcionados

    def remover_aresta(self, v1, v2):
        self.qtd_aresta -= 1
        self.matriz[v1-1][v2-1] = 0
        self.matriz[v2-1][v1-1] = 0

    def existe_aresta(self, v1, v2):
        aresta = self.matriz[v1-1][v2-1]
        if(aresta != 0):
            print(f"Possui aresta entre os vertices {v1} e {v2}: {aresta}")
            return ""
        print("Não existe aresta entre os vertices informados.")

    def checagem_quantidade_de_vertice(self):
        print(f"Quantidade de vertice: {self.num_vertices}")
    
    def checagem_quantidade_de_aresta(self):
        print(f"Quantidade de aresta: {self.qtd_aresta}")

    def exibir(self):
        for index, linha in enumerate(self.matriz):
            print(f"{index} = {linha}")
            # print(linha)


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
