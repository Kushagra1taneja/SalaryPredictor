#importing the libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

#Importing the dataset
dataset=pd.read_csv(r'D:\ML\Projects\SalaryPredictor\Salary_Data.csv')
X=dataset.iloc[:, :-1].values
Y=dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
rgr=LinearRegression() 
rgr.fit(X_train,y_train)

y_pred=rgr.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,rgr.predict(X_train),color='red')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience - training set")
plt.show()

# Visualising the Test set results
plt.scatter(X_test,y_test,color='blue')
plt.plot(X_train,rgr.predict(X_train),color='red')
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary vs Experience - test set")
plt.show()

#Predicting the salary for x years of experience
print("Enter the years of experience to predict the salary: ")
x=float(input())
print("Salary predicted (in $) is:",list(rgr.predict([[x]]))[0].round(2))
