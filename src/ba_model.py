import networkx as nx

MCU = nx.Graph()

MCU = nx.barabasi_albert_graph(350, 1)

nx.write_gml(MCU, "ba_model.gml")