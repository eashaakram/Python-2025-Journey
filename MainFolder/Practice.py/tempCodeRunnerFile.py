import pandas as pd
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