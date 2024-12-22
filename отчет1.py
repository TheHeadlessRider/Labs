import networkx as nx
import timeit

# Создание направленного графа
G = nx.DiGraph()

G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)

# Сортировка и вывод ребер для каждой вершины
for node, edges in G.adjacency():
    sorted_edges = sorted(edges.items(), key=lambda x: x[0])
    print(f"Вершина {node}: {sorted_edges}")

# Функция для тестирования сортировки ребер
def test_sort_edges():
    G = nx.DiGraph()
    G.add_edges_from([(1, 3), (1, 2), (2, 4), (3, 4)])
    for node, edges in G.adjacency():
        sorted_edges = sorted(edges.items(), key=lambda x: x[0])
        assert sorted_edges == list(sorted(edges.items(), key=lambda x: x[0]))

# Измерение времени выполнения сортировки
execution_time = timeit.timeit(lambda: sorted(G.adjacency()), number=100)
print(f"Время выполнения для графа: {execution_time}")
