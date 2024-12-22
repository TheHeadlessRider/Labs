from collections import deque
import unittest

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, capacity): # Добавляет ребро с пропускной способностью capacity из u в v
        self.graph[u][v] = capacity

    def bfs(self, source, sink, parent): # Поиск в ширину (BFS) для поиска увеличивающего пути.

        visited = [False] * self.vertices
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in range(self.vertices):
                if not visited[v] and self.graph[u][v] > 0:  # Существует путь к v
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    def ford_fulkerson(self, source, sink): # Jсновная функция для нахождения максимального потока из source в sink

        parent = [-1] * self.vertices  # Хранение пути
        max_flow = 0  # Начальный поток равен 0

        while self.bfs(source, sink, parent):  # Пока есть увеличивающий путь
            # Найти минимальную пропускную способность в найденном пути
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Обновить остаточные емкости рёбер и обратных рёбер
            v = sink
            while v != source:
                u = parent[v]
                print(f"Updating edge ({u}, {v}): {self.graph[u][v]} - {path_flow}")
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow  # Обратный поток
                v = parent[v]

            max_flow += path_flow
            print(f"Path flow: {path_flow}, Current max flow: {max_flow}")

        return max_flow

# Тесты для проверки работы алгоритма
class TestFordFulkerson(unittest.TestCase):
    def test_simple_case(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 10)
        graph.add_edge(1, 3, 5)
        graph.add_edge(0, 2, 15)
        graph.add_edge(2, 3, 10)
        self.assertEqual(graph.ford_fulkerson(0, 3), 20)  # Ожидается 20

    def test_no_path(self):
        graph = Graph(3)
        graph.add_edge(0, 1, 10)
        graph.add_edge(1, 2, 0)  # Нет пропускной способности
        self.assertEqual(graph.ford_fulkerson(0, 2), 0)

    def test_cyclic_graph(self):
        graph = Graph(3)
        graph.add_edge(0, 1, 10)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 0, 2)  # Цикл
        self.assertEqual(graph.ford_fulkerson(0, 2), 5)

if __name__ == "__main__":
    # Запуск тестов
    unittest.main()
