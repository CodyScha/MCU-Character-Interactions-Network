import networkx as nx

G = nx.scale_free_graph(350, alpha=.4, beta=0.5, gamma=0.10, create_using="MCU-1.gml", seed=None, initial_graph="MCU-1.gml")
G.remove_edges_from(nx.selfloop_edges(G))

nx.write_gml(G, "bussin.gml")
