import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------------------------------
# Controle de tipo de grafo
direcionado = True  # 🔁 altere para True ou False
inicio = ''
# ------------------------------------------------------

# Criação do grafo de acordo com o tipo
G = nx.DiGraph() if direcionado else nx.Graph()

# Adicionando nós
G.add_node("A", tipo="Letra", cor="azul")
G.add_node("B", tipo="Letra")
G.add_node("C", tipo="Numero")
G.add_node("D", tipo="Numero")
G.add_node("E", tipo="Numero")

# Adicionando arestas com pesos
G.add_edge("A", "B", peso=5)
G.add_edge("A", "C", peso=3)
G.add_edge("A", "D", peso=7)
G.add_edge("B", "D", peso=2)
G.add_edge("C", "D", peso=4)
G.add_edge("D", "E", peso=2)


# ------------------------------------------------------
# Função: Mostrar grafo com pesos
# ------------------------------------------------------
def mostrar_grafo_com_pesos(grafo, direcionado):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)

    # Configuração condicional para setas
    edge_params = {"arrows": direcionado}
    if direcionado:
        edge_params.update({"arrowstyle": "-|>", "arrowsize": 20})

    nx.draw(
        grafo, pos,
        with_labels=True,
        node_size=1000,
        node_color='lightblue',
        font_weight='bold',
        **edge_params
    )

    labels = nx.get_edge_attributes(grafo, 'peso')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

    plt.title(f"Grafo {'Direcionado' if direcionado else 'Não-Direcionado'} com Pesos", fontsize=14)
    plt.axis("off")
    plt.show()
    return pos, labels


# ------------------------------------------------------
# Função: Caminho em profundidade (DFS)
# ------------------------------------------------------
def dfs_caminho(grafo, vertice_inicial):
    visitados = set()
    caminho = []

    def dfs(v):
        visitados.add(v)
        caminho.append(v)
        for vizinho in grafo.neighbors(v):
            if vizinho not in visitados:
                dfs(vizinho)

    dfs(vertice_inicial)
    return caminho


# ------------------------------------------------------
# Função: Detecção de ciclos
# ------------------------------------------------------
def detectar_ciclo(grafo):
    if grafo.is_directed():
        try:
            nx.find_cycle(grafo, orientation="original")
            return True
        except nx.NetworkXNoCycle:
            return False
    else:
        return not nx.is_forest(grafo)


def ciclos_networkx(grafo):
    if grafo.is_directed():
        try:
            return list(nx.simple_cycles(grafo))
        except nx.NetworkXNoCycle:
            return []
    else:
        return list(nx.cycle_basis(grafo))


# ------------------------------------------------------
# Função: Imprimir sequência de graus
# ------------------------------------------------------
def imprimir_sequencia_de_graus(grafo):
    if grafo.is_directed():
        print("\n🔹 O grafo é direcionado — usando grafo subjacente (não-direcionado):")
        grafo_subjacente = grafo.to_undirected()
        sequencia = [grafo_subjacente.degree(n) for n in grafo_subjacente.nodes()]
    else:
        print("\n🔹 O grafo é não-direcionado:")
        sequencia = [grafo.degree(n) for n in grafo.nodes()]

    print(f"Sequência de graus: {sequencia}")
    # for n, d in zip(grafo.nodes(), sequencia):
    #     print(f" - Grau do vértice {n}: {d}")


# ------------------------------------------------------
# Execução
# ------------------------------------------------------
pos, labels = mostrar_grafo_com_pesos(G, direcionado)

inicio = inicio if inicio else 'A'

caminho_dfs = dfs_caminho(G, inicio)
ciclos = ciclos_networkx(G)
tem_ciclo = detectar_ciclo(G)

print(f"\nCaminho em profundidade a partir de '{inicio}': {caminho_dfs}")
print(f"O grafo possui ciclo? {'Sim' if tem_ciclo else 'Não'}")
print(f"Ciclos encontrados: {ciclos}")
imprimir_sequencia_de_graus(G)


# ------------------------------------------------------
# Visualização: DFS
# ------------------------------------------------------
plt.figure(figsize=(8, 6))
edge_params = {"arrows": direcionado}
if direcionado:
    edge_params.update({"arrowstyle": "-|>", "arrowsize": 20})

nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=2, **edge_params)
edges_dfs = list(zip(caminho_dfs[:-1], caminho_dfs[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges_dfs, edge_color='red', width=3, **edge_params)
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1000)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title(f"DFS - {'Grafo Direcionado' if direcionado else 'Grafo Não-Direcionado'}", fontsize=14)
plt.axis("off")
plt.show()


# ------------------------------------------------------
# Visualização: Ciclos
# ------------------------------------------------------
plt.figure(figsize=(8, 6))
nx.draw_networkx_edges(G, pos, edge_color='lightgray', width=2, **edge_params)

edges_ciclos = []
for ciclo in ciclos:
    if len(ciclo) > 1:
        edges_ciclos.extend(list(zip(ciclo, ciclo[1:] + [ciclo[0]])))

if edges_ciclos:
    nx.draw_networkx_edges(G, pos, edgelist=edges_ciclos, edge_color='green', width=3, **edge_params)

nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=1000)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title(f"Detecção de Ciclos - {'Grafo Direcionado' if direcionado else 'Grafo Não-Direcionado'}", fontsize=14)
plt.axis("off")
plt.show()
