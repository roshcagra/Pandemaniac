import sys
import time
import utils

if __name__ == "__main__":
    try:
        start1 = time.time()
        filename = sys.argv[1]
        n = int(sys.argv[2])
        strategy = sys.argv[3]

        graph = utils.read_graph(filename)
        start2 = time.time()
        nodes = utils.strategies[strategy](graph, n)
        end2 = time.time()
        print('Computation Time: %0.3f s' % (end2-start2))
        utils.write_nodes(nodes)
        end1 = time.time()
        print('Total Runtime: %0.3f s' % (end1-start1))

    except:
        print("   Generates output for the given graph according to the given strategy")
        print("   USAGE:   python gen.py [input graph file] [number of seeds] [strategy]")
        print("   EXAMPLE: python gen.py testgraph1.json 10 closeness_centrality")
        print("   AVAILABLE STRATEGIES:")
        for key in utils.strategies:
            print("      " + key)
