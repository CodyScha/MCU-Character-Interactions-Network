import networkx as nx

n=350
p= 0.0047777
G = nx.erdos_renyi_graph(n, p)


nx.connected_components(G)
nx.write_gml(G, "erdos20.gml")