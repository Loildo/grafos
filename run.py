import networkx as nx

G = nx.DiGraph()
G.add_weighted_edges_from([
    (1, 2, 5),
    (2, 3, 2),
    (2, 4, 3),
    (3, 5, 7),
])

dfs_resultado = list(nx.dfs_preorder_nodes(G, source=1))
print("DFS:", dfs_resultado)