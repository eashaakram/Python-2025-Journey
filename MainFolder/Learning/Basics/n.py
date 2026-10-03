# marks = 70
# if marks >= 80:
#     print('Grade A')
# elif marks >= 60:
#     print('Grade B')
# else:
#     print('Grade C')
# print('LOOPS')
# for i in range(5):
#     print(i)
# for i in range(1,5):
#     print(i)
# print('Break Statement')
# for i in range(1,70):
#     if i==6:
#         break
#     print(i)
# print('continue Statement')
# for i in range(1,70):
#     if i==6:
#         continue
#     print(i)

# print('Task 1')
# # 1. Print numbers from 1 to 20
# for i in range(1,21):
#     print(i, end=" ")

# print('\nTask 2')
# # 2. Check if a number is even or odd
# num = int(input("enter a number: "))
# if num%2 == 0:
#     print('Even')
# else:
#     print('Odd')
    
# print('\nTask 3')
# # 3. Print multiplication table of 5
# for i in range(1,11):
#     print("5 x ",i," = ",5*i)

# print('\nTask 4')
# # 4. Find the sum of numbers from 1 to 10
# sum = 0
# for i in range(1,11):
#     sum+=i
# print('Total = ',sum)

# print('Print Star pattern by Nested loop')
# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print()
# 
# graph = {
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':[],
#     'F':[]
# }
# visited = set()
# def dfs(node):
#     if node not in visited:
#         print(node,end=" ")
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(neighbor)
# dfs('A')      
# from collections import deque      
# graph = {
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':[],
#     'F':[]
# }
# def bfs(start):
#     visited = set()
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node,end=" ")
#             visited.add(node)
#             queue.extend(graph[node])
# bfs('A')            

print('\n1 & 2. BFS + Traversal Order')
from collections import deque
graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])
bfs('A')

print('\n3. Shortest Path using BFS')
from collections import deque
def bfs_shortest_path(start, end):
    visited = set()
    queue = deque([[start]])   # store path
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            print("Shortest Path:", path)
            return
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
bfs_shortest_path('A','F')

print('\n4. Count Visited Nodes')
def bfs_count(start):
    visited = set()
    queue = deque([start])
    count = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            count += 1
            queue.extend(graph[node])
    print("Total Visited:", count)
bfs_count('A')

print('\n5. Level-wise BFS (Tree Style)')
def bfs_levels(start):
    visited = set()
    queue = deque([(start,0)])

    while queue:
        node, level = queue.popleft()
        if node not in visited:
            print("Node:", node, "Level:", level)
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, level+1))

bfs_levels('A')