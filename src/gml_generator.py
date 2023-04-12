import os
import networkx as nx

# * Open the MCU CSV
mcu_csv = open("../MCU CSV/MCU_interactions.csv")
mcu_csv_lines = mcu_csv.readlines()

# * trim the newlines off the line
for i in range(0, len(mcu_csv_lines)):
    mcu_csv_lines[i] = mcu_csv_lines[i].strip()

# * Initialize the network
G = nx.Graph()

for line in mcu_csv_lines:
    # * split the line by comma
    split_line = list(set(line.split(",")))
    # print(split_line)
    
    # * remove the empty bits
    if "" in split_line:
        split_line.remove("")
    # print(split_line)

    # * Now, for each line, use a double for loop to make all of the connections
    for i in range(0, len(split_line)):
        for j in range(i+1, len(split_line)):
            print("adding edge", split_line[i],"--", split_line[j])
            G.add_edge(split_line[i], split_line[j])

nx.write_gml(G, "../MCU GML/MCU.gml")