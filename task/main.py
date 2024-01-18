import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' > ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" > ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

def shortest_path(graph, start):
    dist = {node: float('infinity') for node in graph}
    paths = {node: [] for node in graph}
    dist[start] = 0
    priority_queue = [(0, start, [start])]

    while priority_queue:
        cur_dist, cur_node, cur_path = heapq.heappop(priority_queue)

        if cur_dist > dist[cur_node]:
            continue

        for neighbor, weight in graph[cur_node].items():
            distance = cur_dist + weight['weight']

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                new_path = cur_path + [neighbor]
                paths[neighbor] = new_path
                heapq.heappush(priority_queue, (distance, neighbor, new_path))

    return {"path":paths, "dist": dist}


def print_shortest_path(shortest_paths):
    for obj in shortest_paths:
        print(obj, '=>', shortest_paths[obj], '\n')


def print_shortest_path_lengths(shortest_path_lengths):
    for obj in shortest_path_lengths:
        print(obj, '=>', shortest_path_lengths[obj])


G = nx.Graph(name="Карта метро Харкова")
G.add_nodes_from(["Героїв Праці", "Студентська", "Академіка Павлова", "Академіка Барабашова", "Київська", "Пушкінська", "Університет", "Історичний  музей",
                  "Метробудівників", "Захісників України", "Архитектора Бекетова", "Держпром", "Наукова", "Ботанічний сад", "23 серпня", "Олексіївська", "Перемога",
                  "Холодна гора", "Південний вокзал", "Центральний ринок", "Майдан Конституції", "Проспект Гагаріна", "Спортивна", "Завод ім. Малишева", "Турбоатом",
                  "Палац спорту", "Армійська", "Iмени О.С.Масельського", "Тракторний завод", "Індустріальна"])
G.add_weighted_edges_from([("Героїв Праці", "Студентська", 1), ("Студентська", "Академіка Павлова", 2), ("Академіка Павлова", "Академіка Барабашова", 2),
                           ("Академіка Барабашова", "Київська", 3), ("Київська", "Пушкінська", 2), (
    "Пушкінська", "Університет", 2), ("Університет", "Історичний  музей", 2),
    ("Університет", "Держпром", 2), ("Метробудівників", "Захісників України", 2), (
    "Захісників України", "Архитектора Бекетова", 3), ("Архитектора Бекетова", "Держпром", 1),
    ("Держпром", "Наукова", 2), ("Наукова", "Ботанічний сад", 2), ("Ботанічний сад",
                                                                   "23 серпня", 2), ("23 серпня", "Олексіївська", 2), ("Олексіївська", "Перемога", 1),
    ("Холодна гора", "Південний вокзал", 2), ("Південний вокзал",
                                              "Центральний ринок", 2), ("Центральний ринок", "Майдан Конституції", 2),
    ("Майдан Конституції", "Історичний  музей", 5), ("Майдан Конституції",
                                                     "Проспект Гагаріна", 2), ("Проспект Гагаріна", "Спортивна", 2),
    ("Спортивна", "Метробудівників", 2), ("Спортивна", "Завод ім. Малишева", 2), (
    "Завод ім. Малишева", "Турбоатом", 2), ("Турбоатом", "Палац спорту", 2),
    ("Палац спорту", "Армійська", 2), ("Армійська", "Iмени О.С.Масельського", 2),
    ("Iмени О.С.Масельського", "Тракторний завод", 2), ("Тракторний завод", "Індустріальна", 2)])


index_to_color = {0: 'blue', 1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue',
                  8: 'green', 9: 'green', 10: 'green', 11: 'green', 12: 'green', 13: 'green', 14: 'green', 15: 'green', 16: 'green',
                  17: 'red', 18: 'red', 19: 'red', 20: 'red', 21: 'red', 22: 'red', 23: 'red', 24: 'red', 25: 'red', 26: 'red', 27: 'red', 28: 'red', 29: 'red'}

for i, node in enumerate(G.nodes()):
    G.nodes[node]['color'] = index_to_color.get(i, 'blue')

# Draw the graph with node colors
pos = nx.fruchterman_reingold_layout(G)
colors = nx.get_node_attributes(G, 'color').values()
nx.draw(G, pos, with_labels=True, node_color=list(colors))
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print("Кількість вершин: ", G.number_of_nodes(), "\n")
print("Кількість ребер: ", G.number_of_edges(), "\n")
print("Ступень центральності: ", nx.degree_centrality(G), "\n")
print("Близькість вузла", nx.closeness_centrality(G), "\n")
print("Посередництво вузла", nx.betweenness_centrality(G), "\n")

# Display the plot
plt.text(0.5, 0.005, f"{G.name}", transform=plt.gca(
).transAxes, ha='center', fontsize=14)
plt.show()

print("\n\n DFS подорож: \n")
dfs_recursive(G, 'Держпром')

print("\n\n BFS подорож: \n")
bfs_recursive(G, deque(['Держпром']))

print("\n\n")

shortest_paths = shortest_path(G, 'Держпром')

print("Hайкоротші шляхи від станції 'Держпром' до всіх інших станцій\n")
print_shortest_path(shortest_paths["path"])
print("\n\n")

print("Довжини найкоротших шляхів від станції 'Держпром' до всіх інших станцій\n")
print_shortest_path_lengths(shortest_paths["dist"])
