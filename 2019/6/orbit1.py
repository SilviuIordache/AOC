with open("input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

print(content)


def generate_graph(planet_map):
    graph = {}
    for item in planet_map:
        data = item.split(')')
        #print(data)
        planet = data[0]
        satellite = data[1]
        if planet in graph:
            graph[planet].append(satellite)
        else:
            graph[planet] = [satellite]
    #print(graph)
    return graph


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def calc_total_orbits(graph):
    total = 0
    sattellites = get_all_satellites(graph);
    for satellite in sattellites:
        total += len(find_path(graph, 'COM', satellite)) - 1
    return total


def get_all_satellites(graph):
    bodies = []
    for item in graph:
        if graph[item] not in bodies:
            bodies.extend(graph[item])
    return bodies


def get_orbit_transfers(graph, p1, p2):
    path1 = find_path(graph, 'COM', p1)
    path2 = find_path(graph, 'COM', p2)


    #todo find first common in reverse in both paths
    first_common_not_found = True
    for i in path1[::-1]:
        for j in path2[::-1]:
            if i == j and first_common_not_found:
                first_common_not_found = False
                first_common = i
    jumps1 = len(find_path(graph, first_common, p1)) - 2
    jumps2 = len(find_path(graph, first_common, p2)) - 2

    return jumps1 + jumps2



my_graph = generate_graph(content)
print(calc_total_orbits(my_graph))

print(get_orbit_transfers(my_graph, 'SAN', 'YOU'))
