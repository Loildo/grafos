
from GrafoPt1.Grafo import MatrizAdjacencia, MatrizIncidencia, ListaAdjacencia

# Testando a Matriz de Adjacência
print("Matriz de Adjacência:")
# qtd_vertices = int(input("Digite a qtd de vertices: "))
# grafo_adj = MatrizAdjacencia(qtd_vertices)
grafo_adj = MatrizAdjacencia(4)
grafo_adj.adicionar_aresta_e_ponderar(1, 2, 10)
grafo_adj.adicionar_aresta_e_ponderar(1, 3, 10)
grafo_adj.adicionar_aresta_e_ponderar(1, 4, 10)
grafo_adj.adicionar_aresta_e_ponderar(2, 3, 10)
grafo_adj.adicionar_aresta_e_ponderar(2, 4, 10)
grafo_adj.adicionar_aresta_e_ponderar(3, 4, 10)
grafo_adj.exibir()
print("")
grafo_adj.checagem_quantidade_de_aresta()
grafo_adj.grafo_completo()

# rotular_vertice = int(input("Quer rotular os vertices?"))
# if(rotular_vertice == 1): 
#     for i in range(grafo_adj.num_vertices):
#         rotulo = (input("nome vertice: "))
#         grafo_adj.rotulo_vertice(rotulo)

# grafo_adj.rotular_aresta(1,2, "E1\n")
# grafo_adj.rotular_aresta(2,3, "aresta entre 2 e 3\n")
# grafo_adj.busca_nome_aresta("MG","ES") # recebe o rotulo vertices e retorna o nome da aresta
# grafo_adj.busca_nome_aresta("ES","SP") # recebe o rotulo vertices e retorna o nome da aresta
# grafo_adj.lista_rotulo_vertices()
exit()
vertice_1 = int(input("Informe o primeiro vertice: "))
vertice_2 = int(input("Informe o segundo vertice: "))
grafo_adj.adicionar_aresta_e_ponderar(vertice_1, vertice_2)
print(f"Aresta adicionada entre os vertices: {vertice_1} e {vertice_2}")


grafo_adj.exibir()

qtd_arestas = int(input("Informe a qtd de arestas: "))
for i in range(qtd_arestas):
    vertice_1 = int(input("Informe o primeiro vertice: "))
    vertice_2 = int(input("Informe o segundo vertice: "))
    grafo_adj.adicionar_aresta_e_ponderar(vertice_1, vertice_2)
    print(f"Aresta adicionada entre os vertices: {vertice_1} e {vertice_2}")

remover = int(input("Quer remover arestas: \n - Digite 1 para remover\n - Digite 2 para não remover\n"))
if(remover == 2):
    grafo_adj.exibir()
    exit()
else:
    # NÃO TEM VALIDAÇÃO CASO A ARESTA NÃO EXISTA NA MATRIZ
    qtd_arestas = int(input("Informe a qtd de arestas quer remover: "))
    for i in range(qtd_arestas):
        vertice_1 = int(input("Informe o primeiro vertice: "))
        vertice_2 = int(input("Informe o segundo vertice: "))
        grafo_adj.remover_aresta(vertice_1, vertice_2)
        print(f"Aresta entre os vertices {vertice_1} e {vertice_2} removida.")
    print("\nNova Matriz")
    grafo_adj.exibir()

    
# grafo_adj.adicionar_aresta_e_ponderar(2, 3)
# grafo_adj.exibir()
# grafo_adj.remover_aresta(2, 3)
# print("")
# print("")
# grafo_adj.exibir()

# Testando a Matriz de Incidência
# print("\nMatriz de Incidência:")
# grafo_inc = MatrizIncidencia(5, 3)
# grafo_inc.adicionar_aresta(0, 1)
# grafo_inc.adicionar_aresta(1, 2)
# grafo_inc.exibir()

# # Testando a Lista de Adjacência
# print("\nLista de Adjacência:")
# grafo_lista = ListaAdjacencia(5)
# grafo_lista.adicionar_aresta(0, 1)
# grafo_lista.adicionar_aresta(1, 2)
# grafo_lista.exibir()
