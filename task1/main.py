import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end='>')
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
        print(vertex, end=">")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


G = nx.Graph(name="Карта метро Харкова")
G.add_nodes_from(["Героїв Праці", "Студентська", "Академіка Павлова", "Академіка Барабашова", "Київська", "Пушкінська", "Університет", "Історичний  музей",
                  "Метробудівників", "Захісників України", "Архитектора Бекетова", "Держпром", "Наукова", "Ботанічний сад", "23 серпня", "Олексіївська", "Перемога",
                  "Холодна гора", "Південний вокзал", "Центральний ринок", "Майдан Конституції", "Проспект Гагаріна", "Спортивна", "Завод ім. Малишева", "Турбоатом",
                  "Палац спорту", "Армійська", "імени О.С.Масельського", "Тракторний завод", "Індустріальна"])
G.add_edges_from([("Героїв Праці", "Студентська"), ("Студентська", "Академіка Павлова"), ("Академіка Павлова", "Академіка Барабашова"),
                  ("Академіка Барабашова", "Київська"), ("Київська", "Пушкінська"), (
                      "Пушкінська", "Університет"), ("Університет", "Історичний  музей"),
                  ("Університет", "Держпром"), ("Метробудівників", "Захісників України"), (
                      "Захісників України", "Архитектора Бекетова"), ("Архитектора Бекетова", "Держпром"),
                  ("Держпром", "Наукова"), ("Наукова", "Ботанічний сад"), ("Ботанічний сад",
                                                                           "23 серпня"), ("23 серпня", "Олексіївська"), ("Олексіївська", "Перемога"),
                  ("Холодна гора", "Південний вокзал"), ("Південний вокзал",
                                                         "Центральний ринок"), ("Центральний ринок", "Майдан Конституції"),
                  ("Майдан Конституції", "Історичний  музей"), ("Майдан Конституції",
                                                                "Проспект Гагаріна"), ("Проспект Гагаріна", "Спортивна"),
                  ("Спортивна", "Метробудівників"), ("Спортивна", "Завод ім. Малишева"), (
                      "Завод ім. Малишева", "Турбоатом"), ("Турбоатом", "Палац спорту"),
                  ("Палац спорту", "Армійська"), ("Армійська", "імени О.С.Масельського"), ("імени О.С.Масельського", "Тракторний завод"), ("Тракторний завод", "Індустріальна")])


index_to_color = {0: 'blue', 1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue',
                  8: 'green', 9: 'green', 10: 'green', 11: 'green', 12: 'green', 13: 'green', 14: 'green', 15: 'green', 16: 'green',
                  17: 'red', 18: 'red', 19: 'red', 20: 'red', 21: 'red', 22: 'red', 23: 'red', 24: 'red', 25: 'red', 26: 'red', 27: 'red', 28: 'red', 29: 'red'}

for i, node in enumerate(G.nodes()):
    G.nodes[node]['color'] = index_to_color.get(i, 'blue')

# Draw the graph with node colors
pos = nx.fruchterman_reingold_layout(G)
colors = nx.get_node_attributes(G, 'color').values()
nx.draw(G, pos, with_labels=True, node_color=list(colors))

print("Кількість вершин: ", G.number_of_nodes())
print("Кількість ребер: ", G.number_of_edges())
is_connected = nx.is_connected(G)  # True

# Display the plot
plt.text(0.5, 0.005, f"{G.name}", transform=plt.gca(
).transAxes, ha='center', fontsize=14)
plt.show()

print("\n\n DFS подорож: \n")
dfs_recursive(G, 'Держпром')

print("\n\n BFS подорож: \n")
bfs_recursive(G, deque(['Держпром']))

print("\n\n")
