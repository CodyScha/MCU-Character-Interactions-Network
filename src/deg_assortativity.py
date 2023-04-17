import networkx as nx

MCU = nx.Graph()

MCU = nx.read_gml("../MCU GML/MCU.gml")

# * Now, lets try using the louvain clustering to determine assortativity
communities = nx.community.louvain_communities(MCU, seed=0)

for i in range(0, len(communities)):
    communities[i] = list(communities[i])

comm_dict = {}

for i in range(0, len(communities)):
    for j in range(0, len(communities[i])):
        comm_dict[communities[i][j]] = i

nx.set_node_attributes(MCU, comm_dict, name="cluster")

print(nx.attribute_assortativity_coefficient(MCU, "cluster"))