import operator

def highest_degree(G, n):
    G_degrees = dict(map(lambda (k, v): (k, len(v)), G.iteritems()))

    G_sorted = sorted(G_degrees.items(), key=operator.itemgetter(1), reverse=True)

    top_n = [node for (node, _) in G_sorted[0:n]]
    return top_n;
