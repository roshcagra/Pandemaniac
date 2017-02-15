import json
def read_graph(filename):
    with open (filename, "r") as myfile:
        data=myfile.readlines()
    return json.loads(data[0])

def write_nodes(nodes):
    with open("output.txt", 'w') as myfile:
        for _ in range(50):
            for node in nodes:
                myfile.write(node + "\n")
