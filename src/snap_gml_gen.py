import networkx as nx

# * initialize graph
G = nx.Graph()

# * intialize the snap victim index
snap = open("../Snap Victims\snap_victims.txt")
snap_victims = snap.readlines()

# * trim newlines off victims
for i in range(0, len(snap_victims)):
    snap_victims[i] = snap_victims[i].strip()

# * Open the MCU CSV
mcu_csv = open("../MCU CSV/MCU_interactions.csv")
mcu_csv_lines = mcu_csv.readlines()

# * trim the newlines off the line
for i in range(0, len(mcu_csv_lines)):
    mcu_csv_lines[i] = mcu_csv_lines[i].strip()

for line in mcu_csv_lines:
    # * split the line by comma
    split_line = list(set(line.split(",")))
    print(split_line)
    
    # * Now, remove all of the snap victims on the split_line
    temp_split_line = []
    for person in split_line:
        if not person in snap_victims:
            temp_split_line.append(person)
    
    split_line = list(set(temp_split_line))

    print(split_line)
    # exit()
    
    # * remove the empty bits
    if "" in split_line:
        split_line.remove("")
    # print(split_line)

    # * Now, for each line, use a double for loop to make all of the connections
    for i in range(0, len(split_line)):
        for j in range(i+1, len(split_line)):
            print("adding edge", split_line[i],"--", split_line[j])
            G.add_edge(split_line[i], split_line[j])

    if len(split_line) == 1:
        G.add_node(split_line[0])

nx.write_gml(G, "../MCU GML/MCU_snapped.gml")