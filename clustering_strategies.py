import operator
from sklearn import cluster
import utils
import numpy as np

def strategy_template(adj_list, n, method):
    G_degrees = dict(map(lambda (k, v): (k, len(v)), adj_list.iteritems()))
    i_matrix = utils.adjacency_list_to_incidence_matrix(adj_list)

    clusters = method(i_matrix)

    degree_sorted_clusters = []

    for i in range(8):
        curr_cluster = np.where(clusters==i)[0]
        curr_cluster_degrees = dict((k, G_degrees[k]) for k in curr_cluster)
        degree_sorted_cluster = [node for (node, degree) in sorted(curr_cluster_degrees.items(), key=lambda x: x[1], reverse=True)]
        degree_sorted_clusters.append(degree_sorted_cluster)

    size_degree_sorted_clusters = sorted(degree_sorted_clusters, key=lambda x: len(x), reverse=True)

    seed_nodes = []

    n_left = n
    for cluster in size_degree_sorted_clusters:
        if n_left == 0:
            break
        num = min(n_left, len(cluster))
        seed_nodes += cluster[0:num]
        n_left -= num

    return seed_nodes

def spectral_clustering(adj_list, n):
    """
    Returns highest degree nodes from the largest clusters defined by spectral clustering
    """
    return strategy_template(adj_list, n, cluster.spectral_clustering)

def k_means_clustering(adj_list, n):
    """
    Returns highest degree nodes from the largest cluster defined by k-means clustering
    """
    return strategy_template(adj_list, n, cluster.k_means)
