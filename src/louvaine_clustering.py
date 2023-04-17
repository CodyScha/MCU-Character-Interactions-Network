import networkx as nx

MCU = nx.Graph()

MCU = nx.read_gml("..\MCU GML\MCU.gml")

communities = nx.community.louvain_communities(MCU, seed=0)

for i in range(0, len(communities)):
    communities[i] = list(communities[i])

community_dict = {}

for i in range(0, len(communities)):
    for j in range(0, len(communities[i])):
        # print(communities[i][j])
        community_dict[communities[i][j]] = i

nx.set_node_attributes(MCU, community_dict, name="cluster")

# print(G.nodes(data=True))
nx.write_gml(MCU, "..\MCU GML\MCU_louvaine.gml")