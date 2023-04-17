import networkx as nx
import numpy as np

def scale_free_network(n, m, p):
    # create initial connected network
    G = nx.Graph()
    G.add_nodes_from(range(m))
    for i in range(m):
        for j in range(i+1, m):
            G.add_edge(i, j)

    # add new nodes with preferential attachment and rewiring
    for i in range(m, n):
        # set a random value of m between 1 and the current value of m
        m_i = np.random.randint(1, m+1)
        degrees = np.array(list(dict(G.degree()).values()))
        probs = degrees / degrees.sum()
        targets = np.random.choice(list(G.nodes()), size=m_i, replace=False, p=probs)
        G.add_node(i)
        for j in targets:
            if np.random.rand() < p:
                G.add_edge(i, j)
            else:
                rewired = np.random.choice(list(G.nodes()))
                while G.has_edge(i, rewired) or j == rewired:
                    rewired = np.random.choice(list(G.nodes()))
                G.add_edge(i, rewired)

    return G


nx.write_gml(scale_free_network(350, 3, 0.5), "../MCU GML/scale_free.gml")