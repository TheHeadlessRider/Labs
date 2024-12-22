from collections import deque

def bfs(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances

# Пример графа
graph = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [1]
}

# Вывод расстояний от начальной вершины 1
print(bfs(graph, 1))

import unittest

class TestBFS(unittest.TestCase):
    def test_shortest_paths(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        self.assertEqual(bfs(graph, 1), {1: 0, 2: 1, 3: 1, 4: 2})

if __name__ == "__main__":
    unittest.main()

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    distances = {start: 0}

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor] = distances[current] + 1
    return distances

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

import unittest

class TestBFS(unittest.TestCase):
    def test_bfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        result = bfs(graph, 'A')
        expected = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

import timeit

setup_code = """
from __main__ import bfs
graph = {i: [i+1, i+2] for i in range(1000)}
graph[999] = []
"""
test_code = "bfs(graph, 0)"

execution_time = timeit.timeit(test_code, setup=setup_code, number=100)
print(f"Execution time: {execution_time:.4f} seconds")