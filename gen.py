import sys
import utils

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        strategy = sys.argv[3]

        graph = utils.read_graph(filename)
        nodes = utils.strategies[strategy](graph, n)
        utils.write_nodes(nodes)

    except:
        print("   Generates output for the given graph according to the given strategy")
        print("   USAGE:   python gen.py [input graph file] [number of seeds] [strategy]")
        print("   EXAMPLE: python gen.py testgraph1.json 10 closeness_centrality")
        print("   AVAILABLE STRATEGIES:")
        for key in utils.strategies:
            print("      " + key)
