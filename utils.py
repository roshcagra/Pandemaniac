import json
import numpy as np

def read_graph(filename):
    with open (filename, "r") as myfile:
        data=myfile.readlines()
    G_text = json.loads(data[0])
    return {int(k):map(lambda n: int(n), v) for k,v in G_text.items()}

def adjacency_list_to_incidence_matrix(adj_list):
    node_count = len(adj_list)
    inc_matrix = np.empty((node_count, node_count))
    for node, neighbors in adj_list.iteritems():
        for neighbor in neighbors:
            inc_matrix[node][neighbor] = 1
    return inc_matrix

def write_nodes(nodes):
    with open("output.txt", 'w') as myfile:
        for _ in range(50):
            for node in nodes:
                myfile.write(node + "\n")
