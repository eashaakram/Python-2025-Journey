# # actual_cost = {
# #     'A': 7,
# #     'B': 6,
# #     'C': 2,
# #     'D': 1,
# #     'G': 0
# # }

# # # heuristic values
# # h = {
# #     'A': 6,
# #     'B': 5,
# #     'C': 2,
# #     'D': 1,
# #     'G': 0
# # }

# # # check admissibility
# # admissible = True

# # for node in h:
# #     if h[node] > actual_cost[node]:
# #         admissible = False
# #         print(node, "is NOT admissible")

# # if admissible:
# #     print("Heuristic is admissible")

# #another code
# from queue import PriorityQueue
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['G'],
#     'D': ['G'],
#     'G': []
# }

# # heuristic (try changing values here)
# h = {
#     'A': 3,
#     'B': 2,
#     'C': 1,
#     'D': 4,
#     'G': 0
# }
# def best_first(start, goal):
#     pq = PriorityQueue()
#     pq.put((h[start], start))
#     visited = []

#     while not pq.empty():
#         _, node = pq.get()

#         if node not in visited:
#             print(node, end=" ")
#             visited.append(node)

#             if node == goal:
#                 break

#             for neighbor in graph[node]:
#                 pq.put((h[neighbor], neighbor))

# print("Path with current heuristic:")
# best_first('A', 'G')
# #another code of best first search
# def best_first_search(graph, heuristic, start, goal):
#     pq = PriorityQueue()
#     pq.put((heuristic[start], start))
#     visited = set()
#     while not pq.empty():
#         cost, node = pq.get()
#         if node in visited:
#             continue
#         visited.add(node)
#         print(f"Visiting: {node}")
#         if node == goal:
#             return True
#         for neighbor, _ in graph[node]:
#             if neighbor not in visited:
#                 pq.put((heuristic[neighbor], neighbor))
#     return False

# #next code of greedy bfs
from queue import PriorityQueue
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
h = {
    'A': 6, 'B': 4, 'C': 3,
    'D': 7, 'E': 2, 'F': 5,
    'G': 0
}
def greedy_search(start, goal):
    pq = PriorityQueue()
    pq.put((h[start], start))   # (heuristic, node)
    visited = set()
    while not pq.empty():
        h_value, node = pq.get()
        print("Visiting:", node)
        if node == goal:
            print("Goal reached!")
            return
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                pq.put((h[neighbor], neighbor))
greedy_search('A', 'G')