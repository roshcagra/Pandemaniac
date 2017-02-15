import json
def import_graph(filename):
    with open (filename, "r") as myfile:
        data=myfile.readlines()
    return json.loads(data[0])

print import_graph("testgraph1.json")
