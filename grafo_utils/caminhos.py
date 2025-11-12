import networkx as nx
import matplotlib.pyplot as plt

def exibir_caminho_minimo(grafo, inicio, fim):
    try:
        caminho = nx.shortest_path(grafo, inicio, fim, weight="peso")
        distancia = nx.shortest_path_length(grafo, inicio, fim, weight="peso")
    except nx.NetworkXNoPath:
        print(f"\n⚠️ Não existe caminho entre {inicio} e {fim}.")
        return

    print(f"\n🚗 Caminho mínimo de {inicio} a {fim}: {caminho} (distância {distancia})")

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(grafo, seed=42)
    nx.draw(grafo, pos, with_labels=True, node_size=1000, node_color="lightblue", arrows=grafo.is_directed())
    nx.draw_networkx_edges(grafo, pos, edgelist=list(zip(caminho[:-1], caminho[1:])), edge_color="red", width=3)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, "peso"))
    plt.title(f"Caminho mínimo de {inicio} a {fim}")
    plt.axis("off")
    plt.show()

def exibir_arvore_geradora_minima(grafo, vertice_inicial):
    g = grafo.to_undirected() if grafo.is_directed() else grafo
    if not nx.is_connected(g):
        print("\n⚠️ O grafo não é conexo. Não há uma única árvore geradora mínima.")
        return

    mst = nx.minimum_spanning_tree(g, weight="peso")
    print("\n🌲 Árvore Geradora Mínima:")
    for u, v, dados in mst.edges(data=True):
        print(f" - {u} — {v} (peso: {dados['peso']})")

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(mst, seed=42)
    nx.draw(mst, pos, with_labels=True, node_color="lightgreen", node_size=1000)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst, "peso"))
    plt.title(f"Árvore Geradora Mínima (a partir de {vertice_inicial})")
    plt.axis("off")
    plt.show()
