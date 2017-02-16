import sim
import sys
import utils

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        n = int(sys.argv[2])
        m = len(sys.argv) - 3

        graph = utils.read_graph(filename)
        nodes = {}
        for i in range(m):
            key = sys.argv[i + 3]
            nodes[key] = utils.strategies[key](graph, n)
        print(sim.run(graph, nodes))

    except:
        print("   Runs a simulation on a test graph using the provided strategies")
        print("   USAGE:   python run.py [input graph file] [number of seeds] [strategy1] [strategy2] ...")
        print("   EXAMPLE: python run.py testgraph1.json 10 highest_degree closeness_centrality")
        print("   AVAILABLE STRATEGIES:")
        for key in utils.strategies:
            print("      " + key)
