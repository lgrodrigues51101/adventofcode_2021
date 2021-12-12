def can_add(node, path):
    if not node.islower():
        return True
    if node == "start":
        return False
    for i in range(1, len(path)):
        n = path[i]
        if n.islower():
            reps = path.count(n)
            if reps > 1 :
                return path.count(node) == 0
    return True

def find_all_paths(graph, start, end, path=[]):
    # print(path)
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if can_add(node, path):
            newpaths = find_all_paths(graph, node, end, path)
            # print(newpaths)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

file = open("input")

graph = {}

for line in file:
    line = line.strip()
    start = line.split("-")[0]
    end = line.split("-")[1]

    try:
        if not end in graph[start]:
            graph[start].append(end)
    except KeyError:
        graph[start] = []
        graph[start].append(end)

    try:
        if not start in graph[end]:
            graph[end].append(start)
    except KeyError:
        graph[end] = []
        graph[end].append(start)

# print(graph)

paths = find_all_paths(graph, "start", "end")

# for path in paths:
#     print(path)

print(len(paths))