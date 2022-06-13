from sklearn.neighbors import KNeighborsRegressor
import pandas
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import KFold
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import scale
from sklearn.ensemble import RandomForestRegressor
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import PassiveAggressiveRegressor
import matplotlib.pyplot as plt

msft = yf.Ticker("MSFT")
print(msft)
data = yf.download("AAPL", start="2000-08-01", end="2017-09-01")
data_test = yf.download("AAPL", start="2018-08-01", end="2019-09-01")
X = data[['Open', 'High', 'Low']]
y = data['Close']
 
X_test = data_test[['Open', 'High', 'Low']]
y_test = data_test['Close']

def Learning(x,y,method):
	dictionary = {'rfc': RandomForestRegressor, 'knn': KNeighborsRegressor,'PAR': PassiveAggressiveRegressor,'lr': LinearRegression}
	m = method
	new_m = dictionary.get(m)
	argument = input()
	if (argument != ''):
		argument = int(argument)
		new_m = new_m(argument)
	else:
		new_m = new_m()
	cf = new_m.fit(X,y)
	pred = cf.predict(X_test)
	answer = mean_squared_error(y_test, pred)
	
	
	test_loss = np.empty(len(X_test))
	train_loss = np.empty(len(X))
	i = 0
	for y_decision in cf.predict(X):
		#y_decision = 1.0/(1.0 + np.exp(-y_decision))
		train_loss[i] = (y[i] - y_decision) * (y[i] - y_decision)
		i += 1
	i = 0
	for y_decision in cf.predict(X_test):
		#y_decision = 1.0/(1.0 + np.exp(-y_decision))
		test_loss[i] = (y_test[i] - y_decision) * (y_test[i] - y_decision)
		i += 1
	plt.figure()
	plt.scatter([i for i in range(len(test_loss))], test_loss)
	plt.scatter([i for i in range(len(train_loss))], train_loss)
	plt.legend(['test', 'train'])
	plt.xlabel('some_x_label', fontsize=12)
	plt.ylabel('some_y_label', fontsize=12)
	plt.title('some_title', fontsize=12)
	plt.gcf().set_size_inches((45, 15))
	g = plt.show()
	c = cf.predict(X_test)
	return answer, g, c[:10]
method = input()
print(Learning(X,y, method))

print()
#y от xn и временной ряд