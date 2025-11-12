import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo(grafo, direcionado, titulo="Grafo"):
    pos = nx.spring_layout(grafo, seed=42)
    edge_params = {"arrows": direcionado}
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
    plt.title(titulo)
    plt.axis("off")
    plt.show()


def mostrar_dfs(grafo, caminho, arestas_dfs):
    """
    Exibe graficamente o grafo destacando a árvore DFS.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)

    edge_params = {"arrows": grafo.is_directed()}
    if grafo.is_directed():
        edge_params.update({"arrowstyle": "-|>", "arrowsize": 20})

    # Arestas do grafo em cinza
    nx.draw_networkx_edges(grafo, pos, edge_color="lightgray", width=2, **edge_params)
    # Arestas da DFS em vermelho
    nx.draw_networkx_edges(grafo, pos, edgelist=arestas_dfs, edge_color="red", width=3, **edge_params)

    # Nós e rótulos
    nx.draw_networkx_nodes(grafo, pos, node_color="skyblue", node_size=1000)
    nx.draw_networkx_labels(grafo, pos, font_size=12, font_weight="bold")

    # Exibir pesos das arestas
    labels = nx.get_edge_attributes(grafo, "peso")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

    plt.title(f"Árvore DFS a partir do vértice '{caminho[0]}'", fontsize=14)
    plt.axis("off")
    plt.show()


def mostrar_bfs(grafo, caminho, arestas_bfs):
    """
    Exibe graficamente o grafo destacando a árvore BFS.
    """
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)

    edge_params = {"arrows": grafo.is_directed()}
    if grafo.is_directed():
        edge_params.update({"arrowstyle": "-|>", "arrowsize": 20})

    # Arestas do grafo em cinza
    nx.draw_networkx_edges(grafo, pos, edge_color="lightgray", width=2, **edge_params)
    # Arestas da BFS em verde
    nx.draw_networkx_edges(grafo, pos, edgelist=arestas_bfs, edge_color="green", width=3, **edge_params)

    # Nós e rótulos
    nx.draw_networkx_nodes(grafo, pos, node_color="lightblue", node_size=1000)
    nx.draw_networkx_labels(grafo, pos, font_size=12, font_weight="bold")

    # Pesos das arestas
    labels = nx.get_edge_attributes(grafo, "peso")
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

    plt.title(f"Árvore BFS a partir do vértice '{caminho[0]}'", fontsize=14)
    plt.axis("off")
    plt.show()
