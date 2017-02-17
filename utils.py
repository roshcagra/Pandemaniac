import json
import networkx as nx
import numpy as np

import nx_strategies
import clustering_strategies

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
                myfile.write(str(node) + "\n")

def adjacency_list_to_networkx(adj_list):
    G = nx.Graph()
    for node in adj_list:
        G.add_node(node)
        G.add_edges_from([(node, target) for target in adj_list[node]])
    return G

strategies = {
    "highest_degree": nx_strategies.highest_degree,
    "average_neighbor_degree": nx_strategies.average_neighbor_degree,
    "closeness_centrality": nx_strategies.closeness_centrality,
    "communicability_centrality": nx_strategies.communicability_centrality,
    "eigenvector_centrality": nx_strategies.eigenvector_centrality,
    "eigenvector_centrality_rand": nx_strategies.eigenvector_centrality_rand,
    "spectral_clustering": clustering_strategies.spectral_clustering,
    "k_means_clustering": clustering_strategies.k_means_clustering,
}
