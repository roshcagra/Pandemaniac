import operator
import networkx as nx
import utils

def strategy_template(adj_list, n, method):
    G = utils.adjacency_list_to_networkx(adj_list)
    degrees = method(G)
    topDegrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    return [node for (node, _) in topDegrees[:n]]

def highest_degree(adj_list, n):
    """
    Returns n nodes from G that have the highest degree
    """
    return strategy_template(adj_list, n, nx.degree)

def average_neighbor_degree(adj_list, n):
    """
    Returns n nodes from G that have the highest average neighbor degree
    """
    return strategy_template(adj_list, n, nx.average_neighbor_degree)

def closeness_centrality(adj_list, n):
    """
    Returns n nodes from G that have the where the sum of the shortest paths
    from a node to the rest of the nodes is the smallest
    """
    return strategy_template(adj_list, n, nx.closeness_centrality)

def communicability_centrality(adj_list, n):
    """
    Returns n nodes from G that have the where the sum of the all closed walks
    starting and ending at the node is the smallest
    """
    return strategy_template(adj_list, n, nx.communicability_centrality)
