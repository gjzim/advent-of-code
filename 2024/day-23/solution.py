from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip()

lines = data.split("\n")
graph = defaultdict(set)
for line in lines:
    u, v = line.split('-')
    graph[u].add(v)
    graph[v].add(u)

def three_node_cliques():
    cliques = set()
    for node, edges in graph.items():
        if node[0] != 't':
            continue

        for first in edges:
            for second in edges:
                if first != second and first in graph[second]:
                    clique = tuple(sorted([node, first, second]))
                    cliques.add(clique)

    return cliques

def bron_kerbosch(R, P, X):
    if not P and not X:
        clique = ','.join(sorted(list(R)))
        yield clique

    while P:
        v = P.pop()
        yield from bron_kerbosch(
            R | {v},
            P & graph[v],
            X & graph[v]
        )
        X.add(v)

solution1 = len(three_node_cliques())
solution2 = max(bron_kerbosch(set(), set(graph.keys()), set()), key = len)
print(solution1)
print(solution2)