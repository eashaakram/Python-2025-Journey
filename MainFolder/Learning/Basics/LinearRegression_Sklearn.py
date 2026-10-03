# # import pandas as pd

# # from sklearn.datasets import fetch_openml
# # from sklearn.model_selection import train_test_split
# # from sklearn.linear_model import LinearRegression

# # # Load Boston dataset
# # boston = fetch_openml(
# #     name='boston',
# #     version=1,
# #     as_frame=True,
# #     parser='auto'
# # )

# # # Use the data directly as a DataFrame
# # df = boston.frame

# # # Independent variable (X)
# # X = df[['RM']]

# # # Target variable (y)
# # y = boston.target

# # # Train-test split
# # X_train, X_test, y_train, y_test = train_test_split(
# #     X,
# #     y,
# #     test_size=0.2,
# #     random_state=42
# # )

# # # Create and train model
# # model = LinearRegression()

# # model.fit(X_train, y_train)

# # # Display coefficients
# # print("Slope (m):", model.coef_[0])

# # print("Intercept (c):", model.intercept_)

# # #for one feature 
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from sklearn import datasets, linear_model
# # from sklearn.metrics import mean_squared_error

# # diabetes = datasets.load_diabetes()
# # diabetes_X = diabetes.data[:,np.newaxis,2]
# # #print(diabetes_X) if we go with this it will create plot big graph
# # # so we sliced it
# # diabetes_X_train = diabetes_X[:-30] #last thirty laa lia
# # diabetes_X_test = diabetes_X[-30:] #starting ka 20

# # diabetes_y_train = diabetes.target[:-30]
# # diabetes_y_test = diabetes.target[-30:]

# # model = linear_model.LinearRegression()

# # model.fit(diabetes_X_train, diabetes_y_train)

# # diabetes_y_predicted= model.predict(diabetes_X_test) 

# # print('Mean Squared error is ',mean_squared_error(diabetes_y_test,diabetes_y_predicted))

# # print('Weights: ',model.coef_)
# # print('Intercept: ',model.intercept_)

# # plt.scatter(diabetes_X_test,diabetes_y_test)
# # plt.plot(diabetes_X_test,diabetes_y_predicted)

# # plt.show()
# #output
# # Mean Squared error is  3035.060115291269
# # Weights:  [941.43097333]
# # Intercept:  153.39713623331644


# #for multiple features modify upper code 
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error

# diabetes = datasets.load_diabetes()
# diabetes_X = diabetes.data
# #print(diabetes_X) if we go with this it will create plot big graph
# # so we sliced it
# diabetes_X_train = diabetes_X[:-30] #last thirty laa lia
# diabetes_X_test = diabetes_X[-30:] #starting ka 20

# diabetes_y_train = diabetes.target[:-30]
# diabetes_y_test = diabetes.target[-30:]

# model = linear_model.LinearRegression()

# model.fit(diabetes_X_train, diabetes_y_train)

# diabetes_y_predicted= model.predict(diabetes_X_test) 

# print('Mean Squared error is ',mean_squared_error(diabetes_y_test,diabetes_y_predicted))

# print('Weights: ',model.coef_)
# print('Intercept: ',model.intercept_)

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Sample dataset: Years of Experience vs. Salary
data = {
'Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'Salary': [35000, 40000, 50000, 60000, 65000, 70000, 85000, 90000, 95000, 100000]
}
df = pd.DataFrame(data)
# Split dataset
X = df[['Experience']] # Independent variable
y = df['Salary'] # Dependent variable
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Display coefficients
print("Slope (m):", model.coef_[0])
print("Intercept (c):", model.intercept_)
# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nMean Squared Error:", mse)
print("R2 Score:", r2)
# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Linear Regression: Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()