import operator

def anti_highest_degree(G, n):
    selected = set()
    def chooseNode(node):
        if len(selected) < n and node not in selected:
            selected.add(node)

    G_degrees = dict(map(lambda (k, v): (k, len(v)), G.iteritems()))

    G_sorted = sorted(G_degrees.items(), key=operator.itemgetter(1), reverse=True)

    for (node, _) in G_sorted:
        if len(selected) == n:
            break
        try:
            chooseNode(G[node][0])
            chooseNode(G[node][1])
        except:
            print "Error Choosing Node"

    assert(n == len(selected))

    return list(selected)
