import networkx as nx

MCU = nx.Graph()

MCU = nx.read_gml("../MCU GML/MCU.gml")

pathsfile = open("../Shortest Paths/shortest_paths.csv", "w")

lengths = dict(nx.all_pairs_shortest_path_length(MCU))

lengths_list = []

for node in MCU.nodes:
    for node2 in MCU.nodes:
        if node2 in lengths[node].keys():
            print(node)
            print(node2)
            leng = lengths[node][node2]
            if leng != 0:
                pathsfile.write(str(leng) + "\n")
                lengths_list.append(leng)

lengths_set = set(lengths_list)

# init dictionary
