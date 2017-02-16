import json
import networkx as nx
import numpy as np

def read_graph(filename):
    with open (filename, "r") as myfile:
        data=myfile.readlines()
    return json.loads(data[0])

def adjacency_list_to_incidence_matrix(adj_list):
    node_count = len(adj_list)
    inc_matrix = np.empty((node_count, node_count))
    for node, neighbors in adj_list.iteritems():
        int_node = int(node)
        for neighbor in neighbors:
            inc_matrix[int_node][int(neighbor)] = 1
    return inc_matrix

def write_nodes(nodes):
    with open("output.txt", 'w') as myfile:
        for _ in range(50):
            for node in nodes:
                myfile.write(node + "\n")

def adjacency_list_to_networkx(adj_list):
    G = nx.Graph()
    for node in adj_list:
        G.add_node(node)
        G.add_edges_from([(node, target) for target in adj_list[node]])
    return G
