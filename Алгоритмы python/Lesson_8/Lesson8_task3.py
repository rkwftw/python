# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором
# все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_create(n):
    return {i: {j for j in range(random.randint(1, n), random.randint(2, n + 1)) if j != i} for i in range(1, n + 1)}


def deep(graph, vertex, visited):
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            deep(graph, neighbour, visited)


num = int(input('Введите число вершин: '))
g = graph_create(num)

visited = set()
num_components = 0
for v in g:
    if v not in visited:
        deep(g, v, visited)
        num_components += 1


print(*g.items(), sep='\n')
print(f'Количество компонент связанности: {num_components}')
print(visited)