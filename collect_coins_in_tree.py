# Solution for collecting coins in a tree with distance 2 reach
from collections import deque, defaultdict


def collect_the_coins(coins, edges):
    n = len(coins)
    graph = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # First pass: remove leaves without coins
    q = deque([i for i in range(n) if degree[i] == 1 and coins[i] == 0])
    removed = [False] * n
    while q:
        u = q.popleft()
        removed[u] = True
        for v in graph[u]:
            if removed[v]:
                continue
            degree[v] -= 1
            if degree[v] == 1 and coins[v] == 0:
                q.append(v)

    # Second pass: remove leaves twice (distance 2 collection)
    q = deque([i for i in range(n) if degree[i] == 1 and not removed[i]])
    for _ in range(2):
        size = len(q)
        for _ in range(size):
            u = q.popleft()
            removed[u] = True
            for v in graph[u]:
                if removed[v]:
                    continue
                degree[v] -= 1
                if degree[v] == 1:
                    q.append(v)

    # Count remaining edges
    remaining_edges = 0
    for u in range(n):
        if removed[u]:
            continue
        for v in graph[u]:
            if u < v and not removed[v]:
                remaining_edges += 1
    return remaining_edges * 2


if __name__ == "__main__":
    tree_nodes = 11
    tree_to = [1, 2, 6, 3, 4, 10, 5, 7, 8, 9]
    tree_from = [0, 0, 0, 1, 1, 3, 4, 6, 7, 8]
    coins = [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1]
    edges = list(zip(tree_from, tree_to))
    result = collect_the_coins(coins, edges)
    print("Minimal edges traversed:", result)
