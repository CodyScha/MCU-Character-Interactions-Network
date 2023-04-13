import networkx as nx

G = nx.Graph()

G = nx.barabasi_albert_graph(350, 1)

nx.write_gml(G, "ba_model.gml")