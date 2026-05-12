# import pandas as pd

# from sklearn.datasets import fetch_openml
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# # Load Boston dataset
# boston = fetch_openml(
#     name='boston',
#     version=1,
#     as_frame=True,
#     parser='auto'
# )

# # Use the data directly as a DataFrame
# df = boston.frame

# # Independent variable (X)
# X = df[['RM']]

# # Target variable (y)
# y = boston.target

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# # Create and train model
# model = LinearRegression()

# model.fit(X_train, y_train)

# # Display coefficients
# print("Slope (m):", model.coef_[0])

# print("Intercept (c):", model.intercept_)
