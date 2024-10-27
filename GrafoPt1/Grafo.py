

class MatrizAdjacencia:
    def __init__(self, num_vertices):
        self.qtd_aresta = 0
        self.num_vertices = num_vertices
        self.lista_rotulo_vertice = ["MG", "ES", "SP"]
        self.matriz = [[0] * num_vertices for i in range(num_vertices)]
        self.matriz_rotulo_aresta = [[0] * num_vertices for i in range(num_vertices)]

    def adicionar_aresta_e_ponderar(self, v1, v2, ponderacao):
        self.qtd_aresta += 1 
        self.matriz[v1-1][v2-1] = ponderacao
        self.matriz[v2-1][v1-1] = ponderacao  # Para grafos não direcionados
    
    def rotular_aresta(self, v1, v2, rotulo):
        self.matriz_rotulo_aresta[v1-1][v2-1] = rotulo
        self.matriz_rotulo_aresta[v2-1][v1-1] = rotulo

    def busca_nome_aresta(self, v1, v2):
        for index, vertice in enumerate(self.lista_rotulo_vertice):
            if(vertice == v1):
                v1 = index
            if(vertice == v2):
                v2 = index
        nome_aresta = self.matriz_rotulo_aresta[v1][v2]
        print(nome_aresta)
        
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
        print(self.matriz[0])
        for index, linha in enumerate(self.matriz):
            # print(f"{self.lista_rotulo_vertice[index]}  = {linha}")
            print(f"{index} = {linha}")

    def rotulo_vertice(self, rotulo):
        self.lista_rotulo_vertice.append(rotulo)
        print("Vertice rotulado")

    def ponderar_vertice(self, ponderacao):
        print("não tá feito!")

    def lista_rotulo_vertices(self): 
        print(self.lista_rotulo_vertice)

    def grafo_completo(self):
        resultado_formula = (self.num_vertices * (self.num_vertices - 1)) / 2
        if(resultado_formula == self.qtd_aresta):
            return print("É um grafo completo")

        return print("Não é um grafo completo")

    def grafo_vazio(self):
        if(self.qtd_aresta == 0 & self.num_vertices != 1): 
            return print("O grafo é um grafo vazio")
        return print("O grafo possui pelo menos uma aresta")

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
