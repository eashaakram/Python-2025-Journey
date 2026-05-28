# # # actual_cost = {
# # #     'A': 7,
# # #     'B': 6,
# # #     'C': 2,
# # #     'D': 1,
# # #     'G': 0
# # # }

# # # # heuristic values
# # # h = {
# # #     'A': 6,
# # #     'B': 5,
# # #     'C': 2,
# # #     'D': 1,
# # #     'G': 0
# # # }

# # # # check admissibility
# # # admissible = True

# # # for node in h:
# # #     if h[node] > actual_cost[node]:
# # #         admissible = False
# # #         print(node, "is NOT admissible")

# # # if admissible:
# # #     print("Heuristic is admissible")

# # #another code
# # from queue import PriorityQueue
# # graph = {
# #     'A': ['B', 'C'],
# #     'B': ['D'],
# #     'C': ['G'],
# #     'D': ['G'],
# #     'G': []
# # }

# # # heuristic (try changing values here)
# # h = {
# #     'A': 3,
# #     'B': 2,
# #     'C': 1,
# #     'D': 4,
# #     'G': 0
# # }
# # def best_first(start, goal):
# #     pq = PriorityQueue()
# #     pq.put((h[start], start))
# #     visited = []

# #     while not pq.empty():
# #         _, node = pq.get()

# #         if node not in visited:
# #             print(node, end=" ")
# #             visited.append(node)

# #             if node == goal:
# #                 break

# #             for neighbor in graph[node]:
# #                 pq.put((h[neighbor], neighbor))

# # print("Path with current heuristic:")
# # best_first('A', 'G')
# # #another code of best first search
# # def best_first_search(graph, heuristic, start, goal):
# #     pq = PriorityQueue()
# #     pq.put((heuristic[start], start))
# #     visited = set()
# #     while not pq.empty():
# #         cost, node = pq.get()
# #         if node in visited:
# #             continue
# #         visited.add(node)
# #         print(f"Visiting: {node}")
# #         if node == goal:
# #             return True
# #         for neighbor, _ in graph[node]:
# #             if neighbor not in visited:
# #                 pq.put((heuristic[neighbor], neighbor))
# #     return False

# # #next code of greedy bfs
# from queue import PriorityQueue
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['G'],
#     'F': [],
#     'G': []
# }
# h = {
#     'A': 6, 'B': 4, 'C': 3,
#     'D': 7, 'E': 2, 'F': 5,
#     'G': 0
# }
# def greedy_search(start, goal):
#     pq = PriorityQueue()
#     pq.put((h[start], start))   # (heuristic, node)
#     visited = set()
#     while not pq.empty():
#         h_value, node = pq.get()
#         print("Visiting:", node)
#         if node == goal:
#             print("Goal reached!")
#             return
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 pq.put((h[neighbor], neighbor))
# greedy_search('A', 'G')
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# data = {
# 'Experience': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
# 'Salary': [35000,40000,50000,60000,65000,70000,85000,90000,95000,100000,
#            110000,120000,125000,130000,135000,140000,145000,150000,155000,160000]
# }
# data_set = pd.DataFrame(data)
# x=data_set.iloc[:,:-1].values
# y=data_set.iloc[:,1].values
# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)
# reg = LinearRegression()
# reg.fit(x_train, y_train)
# x_pred=reg.predict(x_train)
# plt.scatter(x_train, y_train, color="green", label="Actual(Train)")
# plt.plot(x_train, x_pred, color="red", label="Regression Line")
# plt.title("Salary vs Experience(Training set)")
# plt.xlabel("Years of Expereince")
# plt.ylabel("Salary")
# plt.legend()
# plt.show()



# from sklearn.datasets import load_diabetes
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# diabetes = load_diabetes()
# df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
# X= df[['bmi']]
# y= diabetes.target
# X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("Slope(m): ",model.coef_[0])
# print("Intercept(c): ", model.intercept_)
# mse = mean_squared_error(y_test,y_pred)
# r2=r2_score(y_test,y_pred)
# print("\nMean Square Error: ",mse)
# print("R2 Score: ",r2)

        